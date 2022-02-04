import errno
import shutil
import subprocess

import GenerateSettings

SETTING_NAME = 'hel'  # name for json file
TEST_OPPONENT_NAME = '2016_helios'  # used to run with AutoTest

ROUND_COUNT = 1
GAMES_PER_ROUND = 1
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
    print(f"Setting {i + 1} written! press enter")
    input()
    test_result = subprocess.run(
        ['./test.sh', '-R', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', str(PORT), '-ro', str(ROUND_COUNT), '-t',
         str(GAMES_PER_ROUND), '-n', str(i)], cwd=AUTOTEST_DIR, stdout=subprocess.PIPE)
    print(test_result.stdout.decode('utf-8'))
    i += 1
