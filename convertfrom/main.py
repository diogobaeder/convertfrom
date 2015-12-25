import re
import sys
from decimal import Decimal


SOURCE_PATTERN = re.compile(r'(\d+)\s*(\w+)')
UNIT_MAP = {
    ('m', 'meter', 'meters'): Decimal(1),
    'cm': Decimal(100),
    'mm': Decimal(1000),
}


class ArgParser:
    def __init__(self):
        self.remainings = None
        self.destination_string = None
        self.source_quantity = None
        self.source_unit = None

    def parse(self, args):
        self.remainings = list(args)
        source_parts = self.get_source_parts()
        self.destination_string = self.remainings[0]
        self.source_quantity = Decimal(str(float(source_parts[0])))
        self.source_unit = source_parts[1]

    def get_source_parts(self):
        source_string = self.get_source_string()
        matches = SOURCE_PATTERN.match(source_string)
        source_parts = matches.groups()
        return source_parts

    def get_source_string(self):
        source_tokens = []
        while True:
            token = self.remainings.pop(0)
            if token == 'to':
                break
            source_tokens.append(token)
        source_string = ' '.join(source_tokens)
        return source_string


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
