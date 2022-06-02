import csv
from os.path import join

import hyperopt
import hyperopt.pyll.stochastic
import GenerateSettings
import main
from hyperopt import hp, fmin, tpe, STATUS_OK, Trials

from ResultParser import get_result_data,short_result_to_dict

space = {'ChainAction/ChainDeph': hp.choice('ChainAction/ChainDeph', [1, 2, 3, 4]),
         'ChainAction/ChainNodeNumber': hp.quniform('ChainAction/ChainNodeNumber', 500, 1000, 100),
         }
i = 0
space_sample = hyperopt.pyll.stochastic.sample(space)
space_keys=space_sample.keys()

def objective(space):
    changes_dict = dict()
    for key in space:
        changes_dict[key] = [space[key]]
    all_outputs = GenerateSettings.SettingGenerator(
        main.ORIGINAL_BINARY_ADDRESS + main.SETTING_SUBDIR + main.SETTING_NAME,
        changes_dict).generate()

    all_outputs[0].write_to_file(main.storage_dir, str(i) + '.json')
    values=[]
    for key in space_keys:
        values += [space[key]]
    setting_dst_address = join(main.TEST_BINARY_ADDRESS + main.SETTING_SUBDIR, main.SETTING_NAME)
    res = main.test_setting(join(main.storage_dir,f'{i}.json'), setting_dst_address)

    short_data = get_result_data(res)
    with open(f'./out/{main.TESTNAME}/results/RESULT_{i}', 'w') as res_file:
        res_file.write(res)
    with open(f'./out/{main.TESTNAME}/short_results_csv.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([f'{i}.json', main.TEST_OPPONENT_NAME] + short_data + values)
    short_data_dict=short_result_to_dict(short_data)
    accuracy = short_data_dict['goal_diff']
    return {'loss': -accuracy, 'status': STATUS_OK}


main.remove_previous_binary()
main.copy_binary()
main.backup_old_result()
main.make_output_file_and_directories()

values_dict = '\n'.join(space_sample.keys())
with open(f'./out/{main.TESTNAME}/changed_values', 'w') as f:
    f.write(values_dict)
with open(f'./out/{main.TESTNAME}/short_results_csv.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Filename', 'Opponent', 'Games Played', 'Invalid Games', 'Goal Difference', 'Goals Scored',
                     'Goals Conceded', 'Point Difference', 'Left Point', 'Right Point', 'Winrate',
                     'Expected Winrate'] + space_sample.keys())
trials = Trials()
best = fmin(fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=0,
            trials=trials, )
print(space['ChainAction/ChainDeph'])
print(hyperopt.space_eval(space, best))
