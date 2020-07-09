from typing import List

class BubbleSort:

    '''
        Normal Bubble Sort
    '''

    def sort_integer(self, nums: List[int]):
        n = len(nums)
        no_swap = True
        for i in range(1,n):
            for j in range(0, n-i):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    no_swap = False

            if no_swap == True:
                break

