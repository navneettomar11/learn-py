from typing import List


class RemoveDuplicates:

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        prev = nums[0]
        count = 1
        for i in range(1,n):
            if prev == nums[i]:
                nums[i] = None
            else:
                prev = nums[i]
                count+=1

        while None in nums:
            nums.remove(None)

        return count

if __name__ == '__main__':
    print(RemoveDuplicates().removeDuplicates([1,1,2]))
    print(RemoveDuplicates().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
