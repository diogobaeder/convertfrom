from unittest import TestCase

from nose.tools import istest

from convertfrom.main import main


class EntryPointTest(TestCase):
    @istest
    def converts_10m_to_1000cm(self):
        result = main('10m', 'to', 'cm')

        self.assertEqual(result, 1000)
