import re


def get_winrate(text: str):
    last_segment = text.split("WinRate")[1]
    last_segment = last_segment[:last_segment.index("%")]
    return last_segment


def get_expected_winrate(text: str):
    last_segment = text.split("WinRate")[2]
    last_segment = last_segment[:last_segment.index("%")]
    return last_segment


def get_goaldiff(text: str):
    last_segment = text.split("diff: ")[-2]
    last_segment = last_segment[:last_segment.index(")")]
    return last_segment


def get_avg_point(text: str):
    last_segment = text.split("diff: ")[-1]
    last_segment = last_segment[:last_segment.index(")")]
    return last_segment


def get_result_data(text: str):
    return get_goaldiff(text), get_avg_point(text), get_winrate(text), get_expected_winrate(text)
