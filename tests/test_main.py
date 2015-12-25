from decimal import Decimal
from unittest import TestCase

from nose.tools import istest

from convertfrom.main import main


class EntryPointTest(TestCase):
    @istest
    def converts_10m_to_1000cm(self):
        result = main(['10m', 'to', 'cm'])

        self.assertEqual(result, '1000.0cm')

    @istest
    def converts_1m_to_100cm(self):
        result = main(['1m', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1m_to_1000mm(self):
        result = main(['1m', 'to', 'mm'])

        self.assertEqual(result, '1000.0mm')

    @istest
    def converts_200cm_to_2m(self):
        result = main(['200cm', 'to', 'm'])

        self.assertEqual(result, '2.0m')

    @istest
    def converts_1meter_to_100cm(self):
        result = main(['1meter', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1_meter_to_100cm(self):
        result = main(['1', 'meter', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1_meter_to_1m(self):
        result = main(['1', 'meter', 'to', 'meters'])

        self.assertEqual(result, '1.0meters')
