import sys

from convertfrom.converter import Converter
from convertfrom.parser import ArgParser


def convert(args):
    parser = ArgParser()
    converter = Converter()

    parser.parse(args)
    result = converter.convert(parser)

    return '{}{}'.format(result, parser.destination_string)


def main():
    print(convert(sys.argv[1:]))


if __name__ == '__main__':  # pragma: no cover
    main()
