"""
@ilya-besancon
This program sorts a list of numbers and removes the negative ones.
It uses unit tests to check the functionality of the code.
"""

import unittest


# my test suite:
class TestNegativeSort(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(remove_negs([3, -1, 2, 6]), [2, 3, 6])


def remove_negs(a_list):
    # sorts list in order:
    a_list = sorted(a_list)
    # returns only numbers greater or equal to 0
    return [item for item in a_list if item >= 0]


if __name__ == '__main__':
    # random list of numbers:
    num_list = [4, 32, -14, -7, 25, 8, -3, -2, 4, 0]
    new_list = remove_negs(num_list)
    # shows lists before and after:
    print('Original List: ', num_list)
    print('List without negatives: ', new_list)
    # runs test:
    unittest.main()
