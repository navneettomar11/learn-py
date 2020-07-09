from typing import List

class WaveSort:

    def __swap(self, nums: List[int], i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    '''Array Wave Sorting'''
    def sort(self, nums: List[int]):
        n = len(nums)
        for i in range(0, n, 2):
            if i > 0 and nums[i - 1] > nums[i]:
                self.__swap(nums, i - 1, i)

            if i < n - 1 and nums[i] < nums[i + 1]:
                self.__swap(nums, i, i + 1)

    '''Checking the given array is wave sort'''
    def is_wave_sort(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3 :
            return False

        min_max_min = True if nums[1] > nums[0] and nums[1] > nums[2] else False
        min_max_min_cond = lambda x, y, z : x < y or x < z
        max_min_min_cond = lambda x, y, z : x > y or x > z

        result = True
        for i in range(1, n - 1, 2):
            condition = min_max_min_cond(nums[i], nums[i-1], nums[i+1]) if min_max_min else max_min_min_cond(nums[i], nums[i-1], nums[i+1])
            if condition:
                result = False
                break

        if result == True and n % 2 == 0 and ((min_max_min and nums[n-2] > nums[n-1]) or nums[n-2] < nums[n-1]):
            result = False

        return  result
