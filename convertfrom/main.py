import re
import sys
from decimal import Decimal


SOURCE_PATTERN = re.compile(r'(\d+)\s*(\w+)')
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


def main(args):
    args = list(args)
    source_tokens = []
    while True:
        token = args.pop(0)
        if token == 'to':
            break
        source_tokens.append(token)
    source_string = ' '.join(source_tokens)
    destination_string = args[0]
    matches = SOURCE_PATTERN.match(source_string)
    source_parts = matches.groups()
    source_quantity = Decimal(str(float(source_parts[0])))
    source_unit = source_parts[1]
    destination_multiplier = find_multiplier(destination_string)
    source_multiplier = find_multiplier(source_unit)
    result = source_quantity / source_multiplier * destination_multiplier

    return '{}{}'.format(result, destination_string)


if __name__ == '__main__':  # pragma: no cover
    print(main(sys.argv[1:]))
