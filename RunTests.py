import errno
import os.path
import shutil
import subprocess
from os import listdir
from os.path import isfile, join
from time import sleep

import GenerateSettings

# TODO change finish condition for each setting
# TODO make result script, write result for each setting in file
# TODO use CB instead of start_team
# TODO dont use -R
# TODO fix json name in file and write each setting
TESTNAME = 'testp'
SETTING_NAME = 'hel.json'  # name for json file
TEST_OPPONENT_NAME = '2016_helios'  # used to run with AutoTest

ROUND_COUNT = 5
GAMES_PER_ROUND = 3
PORT = 60000

ORIGINAL_BINARY_ADRESS = '/home/arad/robocup/cyrus/team'  # copy from this
TEST_BINARY_ADDRESS = '../test'  # to this location
SETTING_SUBDIR = '/src/data/settings/'
AUTOTEST_DIR = '/home/arad/AutoTest2D'

# delete previous test binary
try:
    shutil.rmtree(TEST_BINARY_ADDRESS)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
# Copy the content of
# source to destination
try:
    shutil.copytree(ORIGINAL_BINARY_ADRESS, TEST_BINARY_ADDRESS)
except OSError as err:

    # error caused if the source was not a directory
    if err.errno == errno.ENOTDIR:
        shutil.copy2(ORIGINAL_BINARY_ADRESS, TEST_BINARY_ADDRESS)
    else:
        print("Binary Copy Error: % s" % err)
print("Copied binary successfully! press enter")
input()
i = 0
possible_settings = GenerateSettings.SettingGenerator().generate()
for setting in possible_settings:
    setting.write_to_file(TEST_BINARY_ADDRESS + SETTING_SUBDIR, SETTING_NAME)
    setting.write_to_file(f'./out/{TESTNAME}/', str(i) + '.json')
    print(f"Setting {i} written!")
    test_call = subprocess.run(
        ['./test.sh', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', str(PORT), '-ro', str(ROUND_COUNT), '-t',
         str(GAMES_PER_ROUND), '-n', TESTNAME + str(i)], cwd=AUTOTEST_DIR, stdout=subprocess.PIPE)

    print(f"Test {i} started!")
    # test_out_adr = f'{AUTOTEST_DIR}/out/{TESTNAME}{i}/'
    # first_check = False
    # while True:
    #     onlyfiles = [f for f in listdir(test_out_adr) if isfile(join(test_out_adr, f))]
    #     if len(onlyfiles) == 0:
    #         if first_check:
    #             print("Check 2")
    #             break
    #         print("Check 1")
    #         first_check=True
    #     else:
    #         print("Games still running!")
    #         sleep(20)
    test_result = subprocess.run(
        ['./result.sh', '-n',TESTNAME + str(i),"-R","-N"]
        , cwd=AUTOTEST_DIR, stdout=subprocess.PIPE
    )

    print(f"RESULTS FOR TEST {i}")
    print("###################################")
    res = test_result.stdout.decode('utf-8')
    print(test_result.stdout.decode('utf-8'))
    with open(f'./out/{TESTNAME}/{i}_RESULT','w') as res_file:
        res_file.write(res)
    i += 1
