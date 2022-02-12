import errno
import os

import json_handling


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class SettingFile:
    def __init__(self, sample_values: dict):
        self.data = sample_values.copy()

    def clone(self):
        out = SettingFile(self.data)

        return out

    def write_to_file(self, directory, name):
        if directory[-1] != '/':
            directory += '/'
        final_address = f'{directory}{name}'
        mkdir_p(os.path.dirname(final_address))
        json_handling.unflatten_and_write_setting(final_address, self.data)


if __name__ == '__main__':
    test = SettingFile(
        json_handling.read_and_flatten_setting('/home/arad/robocup/cyrus/team/src/data/settings/hel.json'))
    test.write_to_file('./', 'example.json')
