from unittest import TestCase

from nose.tools import istest

from convertfrom.errors import ConversionError
from convertfrom.parser import ArgParser


class ArgParserTest(TestCase):
    def setUp(self):
        self.parser = ArgParser()

    @istest
    def cannot_parse_if_less_than_three_arguments(self):
        with self.assertRaises(ConversionError):
            self.parser.parse([])
