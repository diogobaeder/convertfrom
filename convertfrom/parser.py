import re
from decimal import Decimal

from convertfrom.errors import ConversionError


SOURCE_PATTERN = re.compile(r'(\d+)\s*(\w+)')


class ArgParser:
    def __init__(self):
        self.remainings = None
        self.destination_string = None
        self.source_quantity = None
        self.source_unit = None

    def parse(self, args):
        if len(args) < 3:
            raise ConversionError('Needs at least 3 arguments')
        self.remainings = list(args)
        source_parts = self.get_source_parts()
        self.destination_string = self.remainings[0]
        self.source_quantity = Decimal(str(float(source_parts[0])))
        self.source_unit = source_parts[1]

    def get_source_parts(self):
        source_string = self.get_source_string()
        matches = SOURCE_PATTERN.match(source_string)
        if matches is None:
            raise ConversionError(
                'Unidentifiable pattern in source: {}'.format(source_string))
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
