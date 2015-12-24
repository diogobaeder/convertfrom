import re
import sys
from decimal import Decimal


SOURCE_PATTERN = re.compile(r'(\d+)(\w+)')
UNIT_MAP = {
    'm': Decimal(1),
    'cm': Decimal(100),
    'mm': Decimal(1000),
}


def main(args):
    source_string = args[0]
    destination_string = args[2]
    matches = SOURCE_PATTERN.match(source_string)
    source_parts = matches.groups()
    source_quantity = Decimal(str(float(source_parts[0])))
    source_unit = source_parts[1]
    destination_multiplier = UNIT_MAP[destination_string]
    source_multiplier = UNIT_MAP[source_unit]
    result = source_quantity / source_multiplier * destination_multiplier

    return '{}{}'.format(result, destination_string)


if __name__ == '__main__':  # pragma: no cover
    print(main(sys.argv[1:]))
