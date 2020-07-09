from typing import List

class CycleSort:

    def sort(self, nums: List[int]) -> int:
        n = len(nums)
        writes = 0
        for start in range(0, n):
            item = nums[start]
            pos = start
            for i in range(pos + 1, n):
                if nums[i] < item:
                    pos +=1

            if pos == start:
                continue

            while item == nums[pos]:
                pos += 1

            nums[pos], item = item, nums[pos]
            writes+=1

            while pos != start:
                pos = start
                for i in range(pos + 1, n):
                    if nums[i] < item:
                        pos +=1

                # Put the item there or right after any duplicates.
                while item == nums[pos]:
                    pos += 1
                nums[pos], item = item, nums[pos]
                writes += 1

        return  writes
