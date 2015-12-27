from unittest import TestCase
from unittest.mock import patch

from nose.tools import istest

from convertfrom.main import convert, main


class EntryPointTest(TestCase):
    @istest
    @patch('convertfrom.main.sys')
    @patch('convertfrom.main.print')
    @patch('convertfrom.main.convert')
    def prints_converted_result(self, mock_convert, mock_print, mock_sys):
        mock_sys.argv = ['convertfrom', '2a', 'to', 'b']
        mock_convert.return_value = '2b'

        main()

        mock_print.assert_called_once_with('2b')
        mock_convert.assert_called_once_with(['2a', 'to', 'b'])

    @istest
    @patch('convertfrom.main.convert')
    def exits_on_exceptions(self, mock_convert):
        exception = RuntimeError('oops')
        mock_convert.side_effect = exception

        with self.assertRaises(SystemExit):
            main()


class ConvertTest(TestCase):
    @istest
    def converts_10m_to_1000cm(self):
        result = convert(['10m', 'to', 'cm'])

        self.assertEqual(result, '1000.0cm')

    @istest
    def converts_1m_to_100cm(self):
        result = convert(['1m', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1m_to_1000mm(self):
        result = convert(['1m', 'to', 'mm'])

        self.assertEqual(result, '1000.0mm')

    @istest
    def converts_200cm_to_2m(self):
        result = convert(['200cm', 'to', 'm'])

        self.assertEqual(result, '2.0m')

    @istest
    def converts_1meter_to_100cm(self):
        result = convert(['1meter', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1_meter_to_100cm(self):
        result = convert(['1', 'meter', 'to', 'cm'])

        self.assertEqual(result, '100.0cm')

    @istest
    def converts_1_meter_to_1m(self):
        result = convert(['1', 'meter', 'to', 'meters'])

        self.assertEqual(result, '1.0meters')
