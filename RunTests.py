import errno
import shutil
import subprocess

import GenerateSettings

SETTING_NAME = 'hel'  # name for json file
TEST_OPPONENT_NAME = '2016_helios'  # used to run with AutoTest

ROUND_COUNT = 5
GAMES_PER_ROUND = 10
PORT = 6000

ORIGINAL_BINARY_ADRESS = '/data1/nader/...'  # copy from this
TEST_BINARY_ADDRESS = './test'  # to this location
SETTING_SUBDIR = '/src/data/settings/'
AUTOTEST_DIR = '/data2/arad/AutoTest2D'

possible_settings = GenerateSettings.SettingGenerator().generate()
# Copy the content of
# source to destination
try:
    shutil.copytree(ORIGINAL_BINARY_ADRESS, TEST_BINARY_ADDRESS)
except OSError as err:

    # error caused if the source was not a directory
    if err.errno == errno.ENOTDIR:
        shutil.copy2(ORIGINAL_BINARY_ADRESS, TEST_BINARY_ADDRESS)
    else:
        print("Error: % s" % err)
i = 0
for setting in possible_settings:
    setting.write_to_file(TEST_BINARY_ADDRESS + SETTING_SUBDIR, SETTING_NAME)
    test_result=subprocess.run(['./test.sh', '-R', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', PORT, '-ro', ROUND_COUNT, '-t',
                    GAMES_PER_ROUND, '-n', str(i)], cwd=AUTOTEST_DIR,stdout=subprocess.PIPE)
    print(test_result.stdout)
    i += 1
