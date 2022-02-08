import errno
import shutil
import subprocess

import GenerateSettings
from GenerateFile import mkdir_p
from ResultParser import get_result_data

# TODO make result script, write result for each setting in file
# TODO use CB instead of start_team
# TODO make generation more modular

TESTNAME = 'testp'
SETTING_NAME = 'hel.json'  # name for json file
TEST_OPPONENT_NAME = '2016_helios'  # used to run with AutoTest

ROUND_COUNT = 1
GAMES_PER_ROUND = 1
PORT = 60000

ORIGINAL_BINARY_ADRESS = '/home/arad/robocup/cyrus/team'  # copy from this
TEST_BINARY_ADDRESS = '../test'  # to this location, leave empty to use cb for autotest
SETTING_SUBDIR = '/src/data/settings/'
AUTOTEST_DIR = '/home/arad/AutoTest2D'

#######################################################################################

# delete previous test binary
current_running_test_name = ''
try:
    shutil.rmtree(TEST_BINARY_ADDRESS)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

# Copy the binary
# to destination
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
mkdir_p(f"./out/{TESTNAME}/inputs/")
mkdir_p(f"./out/{TESTNAME}/results/")
with open(f'./out/{TESTNAME}/short_results', 'w') as short_result:
    short_result.write("")
possible_settings = GenerateSettings.SettingGenerator().generate()

for setting in possible_settings:
    setting.write_to_file(TEST_BINARY_ADDRESS + SETTING_SUBDIR, SETTING_NAME)
    setting.write_to_file(f'./out/{TESTNAME}/inputs/', str(i) + '.json')
    print(f"Setting {i} written!")
    current_running_test_name = TESTNAME + str(i)
    test_call = subprocess.run(
        ['./test.sh', '-l', 'test', '-r', TEST_OPPONENT_NAME, '-p', str(PORT), '-ro', str(ROUND_COUNT), '-t',
         str(GAMES_PER_ROUND), '-n', TESTNAME + str(i)], cwd=AUTOTEST_DIR, stdout=subprocess.PIPE)

    print(f"Test {i} started!")
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
        short_result.write(f'{i} {short_data[0]} {short_data[1]} {short_data[2]} {short_data[3]}\n')
    i += 1
