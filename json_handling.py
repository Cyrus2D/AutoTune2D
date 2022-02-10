import json


def flatten_data(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '/')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def unflatten_data(y: dict):
    out={}
    for key in y:
        split_key = key.split('/')
        inner_dict = out
        for key_section in split_key[:-1]:
            if key_section not in inner_dict:
                inner_dict[key_section] = dict()
            inner_dict = inner_dict[key_section]
        inner_dict[split_key[-1]] = y[key]

    return out
def read_and_flatten_setting(json_address):
    data = None
    with open(json_address,'r') as json_file:
        data = json.load(json_file)
    return flatten_data(data)

def unflatten_and_write_setting(json_address:str,flattened_data:dict):
    unflattened = unflatten_data(flattened_data)
    with open(json_address, 'w') as output:
        json.dump(unflattened, output, indent=4)
