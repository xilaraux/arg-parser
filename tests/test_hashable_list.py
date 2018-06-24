import unittest
from hashable_list import List


class TestList(unittest.TestCase):
    def setUp(self):
        self.list = ['t', 'test']

    def test_wrong_hash(self):
        hash_list = List(self.list)

        actual_hash = hash(hash_list)
        expected_hash = hash('wrong string')

        self.assertNotEqual(actual_hash, expected_hash)

    def test_right_hash(self):
        hash_list = List(self.list)

        actual_hash = hash(hash_list)
        expected_hash = hash('|'.join(hash_list))

        self.assertEqual(actual_hash, expected_hash)

    def test_empty_list_representation(self):
        empty_list = List()

        self.assertEqual(repr(empty_list), '')

    def test_full_list_representation(self):
        full_list = List(self.list)

        self.assertEqual(repr(full_list), 't|test')

    def test_hashable_list_comparison(self):
        self.fail('empty test')
