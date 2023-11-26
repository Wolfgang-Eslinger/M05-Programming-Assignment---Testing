# test_my_sum.py

import unittest
from my_sum import sum
print("Script started")

class TestSum(unittest.TestCase):
    
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_tuple(self):
        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
