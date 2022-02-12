# AutoTuner2D
This tool is used to find golden values for settings values. By trying out the combinations that are entered , it will return the setting file that had the best result based on AutoTest.
# How to use
First, input the parameters and values you want to test in GenerateSettings.py (ala the sample entry)
Then input the address and parameters used in AutoTest inside of RunTests.py, and Run the script. wait for it to finish, and then run SortResults.py.
You can change what metric is important (winrate, goal diff, etc.) in SortResults.py as well.