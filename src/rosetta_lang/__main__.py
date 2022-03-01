import sys

from . import parsing

def main(script_path):
    parsing.parse_file(script_path)


if __name__ == "__main__":
    main(sys.argv[1])
