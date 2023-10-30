import argparse
import os
import csv
import subprocess
from datetime import datetime


def sorter_win_rate(x):
    return float(x['Winrate'])


def sorter_expected_win_rate(x):
    return float(x['Expected Winrate'])


def sorter_point(x):
    return float(x['Left Point'])


def f(sort_function):
    if sort_function in ['winrate', 'w']:
        return sorter_win_rate
    if sort_function in ['expected', 'e']:
        return sorter_expected_win_rate
    if sort_function in ['point', 'p']:
        return sorter_point


def sort_result(test_name, sort_function, no_show_options=False):
    file = open(f'out/{test_name}/short_results_csv.csv', 'r')
    rows = csv.reader(file, delimiter=';')
    header = next(rows)
    results = []
    for row in rows:
        res = {}
        for r in range(len(row)):
            res[header[r]] = row[r]
            if no_show_options and header[r] == 'Expected Winrate':
                break

        results.append(res)
    results.sort(key=f(sort_function), reverse=True)
    return header, results


def show_results(test_name, sort_function, show_csv, no_show_options):
    header, results = sort_result(test_name, sort_function, no_show_options)
    if not show_csv:
        for r in results:
            print(r)
    else:
        print(','.join(header))
        for r in results:
            #last = list(r.values())[-1]
            import ast
            #last = ast.literal_eval(last)
            #last = [round(float(l), 1) for l in last]
            #last = [str(l).ljust(4) for l in last]
            line = [x.ljust(7) for x in list(r.values())[:]]
            x = ', '.join(line)
            #x += ','.join(last)
            print(x)


def generate_new_test(test_name, sort_function, new_test_name, selected_number):
    header, results = sort_result(test_name, sort_function)
    if os.path.exists(f'out/{new_test_name}'):
        timestr = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        subprocess.run(['mv', f'out/{new_test_name}', f'out/{new_test_name}_{timestr}'])
    subprocess.run(['mkdir', '-p', f'out/{new_test_name}/inputs'])
    subprocess.run(['cp', f'out/{test_name}/changed_values', f'out/{new_test_name}/'])
    for r in results[:selected_number]:
        file_name = r['Filename']
        subprocess.run(['cp', f'out/{test_name}/inputs/{file_name}', f'out/{new_test_name}/inputs/'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort and Show results')
    parser.add_argument('--test_name', '-n', type=str,
                        help='test name = name of directory in out dir', required=True)
    parser.add_argument('--sort_function', '-s', type=str, default='winrate',
                        help='the name of sorter function=[winrate, ewinrate, point]')
    parser.add_argument('--show_csv', '-csv', action='store_true',
                        help='show result as csv')
    parser.add_argument('--no_show_options', '-noo', action='store_true',
                        help='dont show options')
    parser.add_argument('--new_test_name', '-t', type=str,
                        help='new test name directory')
    parser.add_argument('--selected_number', '-i', type=int,
                        help='number of selected for new test')

    args = parser.parse_args()
    test_name = args.test_name
    sort_function = args.sort_function
    show_csv = args.show_csv
    no_show_options = args.no_show_options
    new_test_name = args.new_test_name
    selected_number = args.selected_number
    print(f'out/{test_name}')
    if not os.path.exists(f'out/{test_name}'):
        print('The short_results_csv.csv is not exist')
        exit(1)
    if new_test_name:
        if new_test_name == test_name:
            print('new test name can not be same as test name')
            exit(1)
        if not selected_number:
            print('you have to identify the number of selected results')
            exit(1)
        generate_new_test(test_name, sort_function, new_test_name, selected_number)
    else:
        show_results(test_name, sort_function, show_csv, no_show_options)