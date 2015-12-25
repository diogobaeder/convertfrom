import sys
from decimal import Decimal

from convertfrom.parser import ArgParser


UNIT_MAP = {
    ('m', 'meter', 'meters'): Decimal(1),
    'cm': Decimal(100),
    'mm': Decimal(1000),
}


def find_multiplier(unit):
    for key, value in UNIT_MAP.items():
        if unit == key or (isinstance(key, (tuple, list)) and unit in key):
            return value
    raise KeyError(repr(unit))


def convert(args):
    parser = ArgParser()
    parser.parse(args)

    destination_multiplier = find_multiplier(parser.destination_string)
    source_multiplier = find_multiplier(parser.source_unit)
    result = (
        parser.source_quantity / source_multiplier * destination_multiplier)

    return '{}{}'.format(result, parser.destination_string)


def main():
    print(convert(sys.argv[1:]))


if __name__ == '__main__':  # pragma: no cover
    main()
