from unittest import TestCase, main
from geeksforgeeks import WaveSort


class TestWaveSort(TestCase):

    def setUp(self) -> None:
        self.waveSort = WaveSort()

    def test_sort(self):
        nums = [10, 5, 6, 3, 2, 20, 100, 80]
        self.waveSort.sort(nums)
        self.assertListEqual(nums, [10, 5, 6, 2, 20, 3, 100, 80])

    def test_is_wave_sort(self):

        nums = [1,2]
        res = self.waveSort.is_wave_sort(nums)
        self.assertFalse(res)

        nums = [1, 5, 3, 7, 2, 8, 6]
        res = self.waveSort.is_wave_sort(nums)
        self.assertTrue(res)

        nums = [10, 5, 6, 2, 20, 3, 100, 80]
        res = self.waveSort.is_wave_sort(nums)
        self.assertTrue(res)

        nums = [1, 2, 3, 4, 5]
        res = self.waveSort.is_wave_sort(nums)
        self.assertFalse(res)

        nums = [1, 5, 3, 7, 2, 1]
        res = self.waveSort.is_wave_sort(nums)
        self.assertFalse(res)

    def tearDown(self):
        self.waveSort = None

if __name__ == "__main__":
    main()
