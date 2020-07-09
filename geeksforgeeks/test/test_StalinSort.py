from unittest import TestCase
from geeksforgeeks import StalinSort


class TestStalinSort(TestCase):

    def setUp(self) -> None:
        self.stalin_sort = StalinSort()

    def tearDown(self) -> None:
        self.stalin_sort = None

    def test_sort(self):
        nums = [2,1,4,3,6,5,8,7,10,9]
        self.stalin_sort.sort(nums)
        self.assertListEqual(nums, [1,2,3,4,5,6,7,8,9,10])

        nums = [9,10,7,8,5,6,3,4,1,2]
        self.stalin_sort.sort(nums)
        self.assertListEqual(nums, [1,2,3,4,5,6,7,8,9,10])

