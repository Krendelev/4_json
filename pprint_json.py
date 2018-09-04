import sys
import json


def load_data(filepath):
    with open(filepath) as handle:
        return json.load(handle)


def pretty_print_json(unformatted_data):
    return json.dumps(unformatted_data, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    try:
        unformatted_json = load_data(sys.argv[1])
    except (IndexError, IOError):
        print("There is no file to prettify")
    except ValueError:
        print("Not a valid JSON file")
    else:
        print(pretty_print_json(unformatted_json))
