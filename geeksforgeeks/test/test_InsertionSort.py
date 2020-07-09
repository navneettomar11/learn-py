from unittest import TestCase

from geeksforgeeks.sort import InsertionSort


class TestInsertionSort(TestCase):

    def setUp(self) -> None:
        self.insertion_sort = InsertionSort()

    def test_sort(self):
        nums = [2,1,4,3,6,5,8,7,10,9]
        self.insertion_sort.sort(nums)
        self.assertListEqual(nums, [1,2,3,4,5,6,7,8,9,10])
