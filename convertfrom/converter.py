from decimal import Decimal


UNIT_MAP = {
    ('m', 'meter', 'meters'): Decimal(1),
    'cm': Decimal(100),
    'mm': Decimal(1000),
}


class Converter:
    def convert(self, parser):
        destination_multiplier = find_multiplier(parser.destination_string)
        source_multiplier = find_multiplier(parser.source_unit)
        result = (
            parser.source_quantity /
            source_multiplier * destination_multiplier)

        return result


def find_multiplier(unit):
    for key, value in UNIT_MAP.items():
        if unit == key or (isinstance(key, (tuple, list)) and unit in key):
            return value
    raise KeyError(unit)
