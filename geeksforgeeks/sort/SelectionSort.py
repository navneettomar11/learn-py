from typing import List

class SelectionSort:

    def sort(self, nums: List[int]):
        n = len(nums)

        for i in range(n):
            min_idx = i
            min_num = nums[i]
            for j in range(i+1, n):
                if min_num > nums[j]:
                    min_num = nums[j]
                    min_idx = j
                j+=1
            if min_idx != i:
                temp = nums[i]
                nums[i] = min_num
                nums[min_idx] = temp


    def sort_strs(self, strings: List[str]):
        n = len(strings)

        for i in range(n):
            min_idx = i
            min_str = strings[i]
            for j in range(i+1, n):
                if min_str > strings[j]:
                    min_idx = j
                    min_str = strings[j]

            if min_idx != i:
                temp = strings[i]
                strings[i] = min_str
                strings[min_idx] = temp

