from typing import List

class InsertionSort:

    def sort(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > num:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = num

