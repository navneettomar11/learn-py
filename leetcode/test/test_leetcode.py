from unittest import TestCase

from leetcode.problems import sort_array_by_parity_bit_ii, shuffle_array, kid_with_candies, smaller_numbers_than_current
from leetcode.problems import running_sum, xor_operations

class Test(TestCase):
    def test_sort_array_by_parity_bit_ii(self):
        sort_array_by_parity_bit_ii([4,2,5,7])

    def test_running_sum_of_1d_array(self):
        self.assertListEqual(running_sum([1,2,3,4]), [1,3,6,10])

    def test_xor_operation(self):
        self.assertEqual(xor_operations(5,0),8)

    def test_shuffle_array(self):
        nums = [2,5,1,3,4,7]
        n = 3
        self.assertListEqual(shuffle_array(nums, n), [2,3,5,4,1,7])

        nums = [1,2,3,4,4,3,2,1]
        n = 4
        self.assertListEqual(shuffle_array(nums, n), [1,4,2,3,3,2,4,1])

        nums = [1,1,2,2]
        n = 2
        self.assertListEqual(shuffle_array(nums, n), [1,2,1,2])

    def test_kid_with_candies(self):
        self.assertListEqual(kid_with_candies([2,3,5,1,3], 3), [True,True,True,False,True])

        self.assertListEqual(kid_with_candies([4,2,1,1,2], 1), [True,False,False,False,False])

        self.assertListEqual(kid_with_candies([12,1,12], 10), [True,False,True])

    def test_smaller_numbers_than_current(self):
        self.assertListEqual(smaller_numbers_than_current([8,1,2,2,3]), [4,0,1,1,3])
        self.assertListEqual(smaller_numbers_than_current([6,5,4,8]), [2,1,0,3])
        self.assertListEqual(smaller_numbers_than_current([7,7,7,7]), [0,0,0,0])
