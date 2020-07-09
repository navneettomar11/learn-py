from typing import List

class StalinSort:

    def sort(self, nums: List[int]):
        j = 0
        n = len(nums)
        while True :
            moved = 0
            for i in range(n-1-j):
                if nums[i] > nums[i + 1]:
                    nums.insert(moved, nums.pop(i+1))
                    moved+=1
            j+=1
            if moved == 0:
                break
