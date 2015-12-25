from unittest import TestCase

from nose.tools import istest

from convertfrom.converter import find_multiplier


class MultiplierTest(TestCase):
    @istest
    def cannot_find_for_inexisting_unit(self):
        with self.assertRaises(KeyError):
            find_multiplier('some-bogus-unit')
