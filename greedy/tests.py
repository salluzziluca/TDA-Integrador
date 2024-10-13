import unittest
from csv_to_array import csv_test_to_array 
from greedy import greedy

class TestGreedy(unittest.TestCase):
    def test_greedy_20(self):
        result = greedy(csv_test_to_array("20.txt"))
        self.assertTrue(result[0]>result[1])


if __name__ == '__main__':
    unittest.main()