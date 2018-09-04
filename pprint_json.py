import sys
import json


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)


def pretty_print_json(data_object):
    return json.dumps(data_object, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    try:
        data_from_json = load_data(sys.argv[1])
    except IndexError:
        print('Please specify path to JSON file')
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Not a valid JSON file')
    else:
        print(pretty_print_json(data_from_json))
