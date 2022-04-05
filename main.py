import errno
import shutil
import subprocess
import signal
import sys
from os import listdir
from os.path import isfile, join

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
GENERATE_SETTINGS = False
USE_CB = False  # SET THIS TO TRUE IF YOU DONT HAVE TEST TEAM CONFIGURED IN START_TEAM OF AUTOTEST


def fill_permutations():
    changes_dict = dict()
    changes_dict['ChainAction/ChainDeph'] = [1, 2, 3]
    changes_dict['ChainAction/ChainNodeNumber'] = [500, 750, 1000]
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
    all_outputs = GenerateSettings.SettingGenerator(ORIGINAL_BINARY_ADDRESS + SETTING_SUBDIR + SETTING_NAME, changes_dict).generate()
    for i in range(len(all_outputs)):
        all_outputs[i].write_to_file(storage_dir, str(i) + '.json')
    print("Settings written to destination!")
    return


def main(generate_settings):
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
    print("Copied binary successfully! press enter")
    input()

    mkdir_p(f"./out/{TESTNAME}/inputs/")
    mkdir_p(f"./out/{TESTNAME}/results/")
    setting_dst_address = join(TEST_BINARY_ADDRESS + SETTING_SUBDIR, SETTING_NAME)
    with open(f'./out/{TESTNAME}/short_results', 'w') as short_result:
        short_result.write(f"{TEST_OPPONENT_NAME} {ROUND_COUNT * GAMES_PER_ROUND}\n")
    changes_dict = fill_permutations()
    if generate_settings:
        SaveSettingsToFile(changes_dict)
    cb_flags = []
    if USE_CB:
        cb_flags = ['-cb', TEST_BINARY_ADDRESS]
    settings_files = sorted([join(storage_dir, f) for f in listdir(storage_dir) if isfile(join(storage_dir, f))])
    for i in range(len(settings_files)):
        shutil.copyfile(settings_files[i], setting_dst_address)
        print("PRESS ENTER")
        input()
        print(f"Test {i} started!")
        test_call = subprocess.run(
            ['./test.sh', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', str(PORT), '-ro', str(ROUND_COUNT), '-t',
             str(GAMES_PER_ROUND), '-n', TESTNAME + str(i)] + cb_flags, cwd=AUTOTEST_DIR, stdout=subprocess.PIPE)

        print(f"Test {i} finshed!")
        test_result = subprocess.run(
            ['./result.sh', '-n', TESTNAME + str(i), "-R", "-N"]
            , cwd=AUTOTEST_DIR, stdout=subprocess.PIPE
        )

        print(f"RESULTS FOR TEST {i}")
        print("###################################")
        res = test_result.stdout.decode('utf-8')
        print(test_result.stdout.decode('utf-8'))
        print("SHORT VERSION")
        short_data = get_result_data(res)
        print()
        with open(f'./out/{TESTNAME}/results/RESULT_{i}', 'w') as res_file:
            res_file.write(res)
        with open(f'./out/{TESTNAME}/short_results', 'a') as short_result:
            short_result.write(f'{i} {short_data[0]} {short_data[1]} {short_data[2]} {short_data[3]} \n')


main(GENERATE_SETTINGS)