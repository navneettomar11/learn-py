from typing import List


class RemoveDuplicates:

    def removeDuplicatesOld(self, nums: List[int]) -> int:
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

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        uniqueCount = 0
        if n < 2:
            return n

        for i in range(n-1, -1, -1):
            if nums[i] == nums[i-1]:
               nums[i] = None
            elif i == 0 or nums[i] != nums[i-1]: uniqueCount+=1

        while None in nums:
            nums.remove(None)

        return uniqueCount

if __name__ == '__main__':
    removeDuplicates = RemoveDuplicates()
    print(removeDuplicates.removeDuplicates([1]))
    print(removeDuplicates.removeDuplicates([1,1,2]))
    print(removeDuplicates.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
