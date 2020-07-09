from unittest import TestCase

from geeksforgeeks import SelectionSort


class TestSelectionSort(TestCase):

    def setUp(self) -> None:
        self.selection_sort = SelectionSort()

    def test_sort(self):
        nums = [2,1,4,3,6,5,8,7,10,9]
        self.selection_sort.sort(nums)
        self.assertListEqual(nums, [1,2,3,4,5,6,7,8,9,10])

    def test_sort_string(self):
        strings = ["paper","true","soap","floppy","flower"]
        self.selection_sort.sort_strs(strings)
        self.assertListEqual(strings, ["floppy", "flower", "paper", "soap", "true"])
