METRIC = 'winrate'  # options are: goal_diff, avg_points, winrate , expected_winrate
TEST_NAME = 'finaltest'

entries = list()
with open(f'./out/{TEST_NAME}/short_results', 'r') as result_file:
    entries = result_file.readlines()
meta_data = entries[0].split()
entries = entries[1:]
for i in range(len(entries)):
    entries[i] = entries[i].split(" ")[:-1]
    entries[i] = list(map(float, entries[i]))
    entries[i][0] = str(int(entries[i][0])) + '.json'  # test number

if METRIC == 'goal_diff':
    entries = sorted(entries, key=lambda x: x[1], reverse=True)
elif METRIC == 'avg_points':
    entries = sorted(entries, key=lambda x: x[2], reverse=True)
elif METRIC == 'winrate':
    entries = sorted(entries, key=lambda x: x[3], reverse=True)
elif METRIC == 'expected_winrate':
    entries = sorted(entries, key=lambda x: x[4], reverse=True)
else:
    raise Exception('Invalid metric!')

print(f'Opponent name: {meta_data[0]}\nGames per test: {meta_data[1]}')
print(f"Sorted settings based on {METRIC}:\n\n")
print(" FILENAME  | GOAL DIFF | AVG POINTS | WINRATE | EXPECTED WINRATE")
print('_' * 64)
for entry in entries:
    print(
        f' {entry[0].ljust(10)}|{str(entry[1]).center(11)}|{str(entry[2]).center(12)}|{str(entry[3]).center(9)}|{str(entry[4]).center(18)}')
