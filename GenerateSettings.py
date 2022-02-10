from GenerateFile import SettingFile
import json_handling


class SettingGenerator:
    def __init__(self, sample_file_address):
        self.data = dict()
        self.base_data = json_handling.read_and_flatten_setting(sample_file_address)
        for key in self.base_data:
            self.data[key] = [self.base_data[key]]
        self.data['ChainAction/ChainDeph']=[1,2,3]
        self.data['ChainAction/ChainNodeNumber'] = [500, 750, 1000]
    def generate(self):
        output = [SettingFile(self.base_data)]
        for key in self.data.keys():
            new_output = []
            for setting in output:
                for value in self.data[key]:
                    new_setting = setting.clone()
                    new_setting.data[key] = value
                    new_output.append(new_setting)
            output = new_output

        return output


if __name__ == '__main__':
    settings = SettingGenerator('/home/arad/robocup/cyrus/team/src/data/settings/hel.json').generate()
    for i in range(len(settings)):
        settings[i].write_to_file('./', str(i + 1))
