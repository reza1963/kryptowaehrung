import unittest
import math
import warnings

from src.util.pandaz import Pandaz

warnings.filterwarnings("ignore")


class TestCase(unittest.TestCase):
    expected_count = 182699

    def test_count(self):
        pandaz = Pandaz("../data/")
        m, p, s = pandaz.dataframes()
        self.assertEqual(len(m) - 1, self.expected_count, 'Record counts is wrong !')
        self.assertEqual(len(p) - 1, self.expected_count, 'Record counts is wrong !')
        self.assertEqual(len(s) - 1, self.expected_count, 'Record counts is wrong !')



if __name__ == '__main__':
    unittest.main()
