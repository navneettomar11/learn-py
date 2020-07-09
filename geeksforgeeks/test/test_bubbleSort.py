from unittest import TestCase

from geeksforgeeks import BubbleSort


class TestBubbleSort(TestCase):

    def setUp(self) -> None:
        self.bubble_Sort = BubbleSort()

    def test_sort_integer(self):
        nums = []
        self.bubble_Sort.sort_integer(nums)
        self.assertListEqual(nums, [])
