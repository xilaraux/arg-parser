import unittest
from args_parser import ArgsParser
from args_parser import ParseError
from hashable_list import List


class TestParser(unittest.TestCase):

    def test_initialization_wih_wrong_template(self):
        with self.assertRaises(ParseError):
            ArgsParser('wrong template')

        with self.assertRaises(ParseError):
            ArgsParser('():')

    def test_initialization_with_right_template(self):
        try:
            ArgsParser('(v|version):string;  (r|red):boolean;')
        except ParseError:
            self.fail('Cannot initialize with right template.')

    def test_initialization_for_one_arg(self):
        parser = ArgsParser('(v|version):string')
        expected_schema = {List(['v', 'version']): 'string'}
        print(parser.schema)

        self.assertDictEqual(parser.schema, expected_schema)

    def test_initialize_for_multiple_args(self):
        parser = ArgsParser('(v|version):string;   (r|red):boolean;   (a|amount):numeric')
        expected_schema = {
            List(['v', 'version']): 'string',
            List(['r', 'red']): 'boolean',
            List(['a', 'amount']): 'numeric'
        }

        self.assertDictEqual(parser.schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
