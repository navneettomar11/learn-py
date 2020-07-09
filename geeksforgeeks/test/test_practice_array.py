import unittest
from geeksforgeeks import sort_array_where_subarray_reversed, is_possible_triange, print_all_triplets


class TestPracticeTest(unittest.TestCase):

    def test_sort_array_where_subarray_reversed(self):
        nums = [2,5,65,55,50,70,90]
        sort_array_where_subarray_reversed(nums)
        self.assertListEqual(nums, [2,5,50,55,65,70,90])


    def test_is_possible_triangel(self):
        nums = [5, 4, 3, 1, 2]
        self.assertTrue(is_possible_triange(nums))

        nums = [4, 1, 2]
        self.assertFalse(is_possible_triange(nums))

    def test_print_all_triplets(self):
        nums = [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]
        result = print_all_triplets(nums)
        self.assertListEqual(result, [[6,9,12], [2,12,22], [12,17,22], [2,17,32],[12,22,32], [9,22,35], [2,22,42], [22,32,42]])







