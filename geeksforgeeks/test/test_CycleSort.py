from unittest import TestCase

from geeksforgeeks import CycleSort


class TestCycleSort(TestCase):

    def setUp(self) -> None:
        self.cycle_sort = CycleSort()

    def test_sort(self):
        nums = [1, 8, 3, 9, 10, 10, 2, 4]
        writes = self.cycle_sort.sort(nums)
        self.assertListEqual(nums, [1,2,3,4,8,9,10,10 ])
