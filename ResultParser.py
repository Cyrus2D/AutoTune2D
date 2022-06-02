import re


def get_game_count(text: str):
    segment = text.split("Game Count: ")[1]
    result = segment[:segment.index('\n')]
    return result


def get_invalid_game_count(text: str):
    return text.count("$$$$")


def get_winrate(text: str):
    last_segment = text.split("WinRate")[1]
    last_segment = last_segment[1:last_segment.index("%")]
    return last_segment


def get_expected_winrate(text: str):
    last_segment = text.split("WinRate")[2]
    last_segment = last_segment[1:last_segment.index("%")]
    return last_segment


def get_goaldiff(text: str):
    last_segment = text.split("diff: ")[-2]
    last_segment = last_segment[:last_segment.index(")")]
    return last_segment


def get_leftgoal(text: str):
    segment = text.split('Avg Goals: ')[1]
    segment = segment[:segment.index(" (")]
    segment = segment.split(' : ')
    return segment[0]


def get_rightgoal(text: str):
    segment = text.split('Avg Goals: ')[1]
    segment = segment[:segment.index(" (")]
    segment = segment.split(' : ')
    return segment[1]


def get_avg_point(text: str):
    last_segment = text.split("diff: ")[-1]
    last_segment = last_segment[:last_segment.index(")")]
    return last_segment


def get_left_points(text: str):
    segment = text.split('Avg Points: ')[1]
    segment = segment[:segment.index(" (")]
    segment = segment.split(' : ')
    return segment[0]


def get_right_points(text: str):
    segment = text.split('Avg Points: ')[1]
    segment = segment[:segment.index(" (")]
    segment = segment.split(' : ')
    return segment[1]


def get_result_data(text: str):
    return [get_game_count(text), get_invalid_game_count(text), get_goaldiff(text), get_leftgoal(text),
            get_rightgoal(text), get_avg_point(text), get_left_points(text), get_right_points(text), get_winrate(text),
            get_expected_winrate(text)]


def short_result_to_dict(input: list):
    result = dict()
    result['game_count'] = input[0]
    result['invalid_game_count'] = input[1]
    result['left_goal'] = input[2]
    result['right_goal'] = input[3]
    result['right_goal'] = input[4]
    result['avg_point'] = input[5]
    result['left_point'] = input[6]
    result['right_point'] = input[7]
    result['win_rate'] = input[8]
    result['expected_win_rate'] = input[9]
    return result


def get_result_dict(text: str):
    return short_result_to_dict(get_result_data(text))


if __name__ == '__main__':
    all_of_it = ''
    with open('./out/yushchain/results/RESULT_[\'1\']', 'r') as file:
        all_of_it = file.read()
    print(get_result_data(all_of_it))
