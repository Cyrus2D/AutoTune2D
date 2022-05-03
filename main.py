import errno
import os
import shutil
import subprocess
import signal
import sys
from datetime import datetime
from os import listdir
from os.path import isfile, join,isdir
import csv
import GenerateSettings
from GenerateFile import mkdir_p
from ResultParser import get_result_data

TESTNAME = 'yushchain'
SETTING_NAME = 'hel.json'  # name for json file
TEST_OPPONENT_NAME = '2021_helios'  # used to run with AutoTest

ROUND_COUNT = 1
GAMES_PER_ROUND = 5
PORT = 60000

ORIGINAL_BINARY_ADDRESS = '/home/arad/robocup/cyrus/team/src'  # copy from this
TEST_BINARY_ADDRESS = '../test'  # to this location
SETTING_SUBDIR = '/data/settings/'
AUTOTEST_DIR = '/home/arad/AutoTest2D'
GENERATE_SETTINGS = True
USE_CB = False  # SET THIS TO TRUE IF YOU DONT HAVE TEST TEAM CONFIGURED IN START_TEAM OF AUTOTEST


def fill_permutations():
    changes_dict = dict()
    changes_dict['ChainAction/ChainDeph'] = [1]
    changes_dict['ChainAction/ChainNodeNumber'] = [1000]
    return changes_dict


##############################
storage_dir = f'./out/{TESTNAME}/inputs/'


# kill currently running test on exit
def exit_handler(signum, frame):
    global TESTNAME
    if TESTNAME != '':
        kill_call = subprocess.run(
            ['./kill.sh', TESTNAME], cwd=AUTOTEST_DIR)
    sys.exit()


signal.signal(signal.SIGINT, exit_handler)


def SaveSettingsToFile(changes_dict: dict):
    global TESTNAME, storage_dir
    all_outputs = GenerateSettings.SettingGenerator(ORIGINAL_BINARY_ADDRESS + SETTING_SUBDIR + SETTING_NAME,
                                                    changes_dict).generate()
    for i in range(len(all_outputs)):
        all_outputs[i].write_to_file(storage_dir, str(i) + '.json')
    print("Settings written to destination!")
    return


def test_setting(json_dir, setting_dst, i):
    setting_file_name = json_dir.split("/")[-1]
    cb_flags = []
    if USE_CB:
        cb_flags = ['-cb', TEST_BINARY_ADDRESS]
    shutil.copyfile(json_dir, setting_dst)
    print(f"Test {setting_file_name} started!")
    test_call = subprocess.run(
        ['./test.sh', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', str(PORT), '-ro', str(ROUND_COUNT), '-t',
         str(GAMES_PER_ROUND), '-n', TESTNAME + str(i)] + cb_flags, cwd=AUTOTEST_DIR, stdout=subprocess.PIPE)

    print(f"Test {setting_file_name} finished!")
    test_result = subprocess.run(
        ['./result.sh', '-n', TESTNAME + str(i), "-R", "-N"]
        , cwd=AUTOTEST_DIR, stdout=subprocess.PIPE
    )

    print(f"RESULTS FOR TEST {setting_file_name}")
    print("###################################")
    res = test_result.stdout.decode('utf-8')
    print(res)
    return res


def main(generate_settings, json_directory=storage_dir):
    # delete previous test binary
    try:
        shutil.rmtree(TEST_BINARY_ADDRESS)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    # Copy the binary
    # to destination
    try:
        shutil.copytree(ORIGINAL_BINARY_ADDRESS, TEST_BINARY_ADDRESS)
    except OSError as err:

        # error caused if the source was not a directory
        if err.errno == errno.ENOTDIR:
            shutil.copy2(ORIGINAL_BINARY_ADDRESS, TEST_BINARY_ADDRESS)
        else:
            print("Binary Copy Error: % s" % err)
    print("Copied binary successfully!")
    if isdir('./out/') and isdir(f'./out/{TESTNAME}/'):
        timestr = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        print(f"Files for {TESTNAME} already exist!\nRenaming previous data to {TESTNAME}_{timestr}")
        os.rename(f'./out/{TESTNAME}',f'./out/{TESTNAME}_{timestr}')
        #shutil.rmtree(f'./out/{TESTNAME}')

    mkdir_p(f"./out/{TESTNAME}/inputs/")
    mkdir_p(f"./out/{TESTNAME}/results/")
    setting_dst_address = join(TEST_BINARY_ADDRESS + SETTING_SUBDIR, SETTING_NAME)
    with open(f'./out/{TESTNAME}/short_results_csv.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'Opponent', 'Games Played','Invalid Games','Goal Difference','Goals Scored','Goals Conceded','Point Difference','Left Point','Right Point','Winrate','Expected Winrate'])
    #with open(f'./out/{TESTNAME}/short_results', 'w') as short_result:
     #   short_result.write(f"{TEST_OPPONENT_NAME} {ROUND_COUNT * GAMES_PER_ROUND}\n")
    changes_dict = fill_permutations()
    if generate_settings:
        SaveSettingsToFile(changes_dict)

    settings_files = sorted(
        [join(json_directory, f) for f in listdir(json_directory) if isfile(join(json_directory, f))])
    for i in range(len(settings_files)):
        setting_file_name = settings_files[i].split("/")[-1]

        res = test_setting(settings_files[i], setting_dst_address, i)
        short_data = get_result_data(res)
        with open(f'./out/{TESTNAME}/results/RESULT_{setting_file_name.split(".")[:-1]}', 'w') as res_file:
            res_file.write(res)
       # with open(f'./out/{TESTNAME}/short_results', 'a') as short_result:
        #    short_result.write(
         #       f'{setting_file_name} {short_data[0]} {short_data[1]} {short_data[2]} {short_data[3]} \n')

        with open(f'./out/{TESTNAME}/short_results_csv.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([setting_file_name,TEST_OPPONENT_NAME]+short_data)

main(GENERATE_SETTINGS)
