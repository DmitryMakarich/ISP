import argparse
from os import path
from serializer import Serializer


parser = argparse.ArgumentParser(description='utility converts from one format to another')
parser.add_argument('-s', '--source', type=str, metavar='',
                    required=True, help="Source config file with extensions - .yaml, .json, .pickle, .toml")
parser.add_argument('-t', '--target', type=str, metavar='',
                    required=True, help="Target config file with another extension")
args = parser.parse_args()


def check_extension(source_file, target_file):
    source_extension = path.splitext(source_file)[1]
    target_extension = path.splitext(target_file)[1]
    valid_extensions = (".json", ".pickle", ".yaml", ".toml")
    if source_extension == target_extension:
        print("Both files have the same extension.")
    if source_extension in valid_extensions and target_extension in valid_extensions:
        return source_file, target_file
    else:
        print("Not supported extension")

    exit()



def main():
    check_extension(args.source, args.target)
    obj = Serializer.deserialize(args.source)
    Serializer.serialize(args.target, obj)


    main()
