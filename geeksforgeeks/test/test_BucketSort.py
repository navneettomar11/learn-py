from unittest import TestCase

from geeksforgeeks import BucketSort


class TestBucketSort(TestCase):

    def setUp(self) -> None:
        self.bucket_sort = BucketSort()

    def tearDown(self) -> None:
        self.bucket_sort  = None

    def test_sort(self):
        nums = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]
        self.bucket_sort.sort(nums)
        self.assertListEqual(nums, [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897])

    def test_sort_with_negative_numbers(self) :
        nums = [-0.897, 0.565, 0.656, -0.1234, 0, 0.3434]
        self.bucket_sort.sort_with_negative_numbers(nums)
        self.assertListEqual(nums, [-0.1234, -0.897, 0, 0.3434, 0.565, 0.656])

