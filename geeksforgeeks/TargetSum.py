from typing import List

class TargetSum:

    def twoSumByTwoPointer(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) -1
        while l != r:
            sum = nums[l] + nums[r]
            if sum == target:
                return list([nums[l], nums[r]])
            elif sum > target:
                r-=1
            else:
                l+=1

        return []

    def twoSumByHashing(self, nums: List[int], target: int) -> List[int]:
        num_Set = set()
        for num in nums:
            if target - num in num_Set:
                return [target-num, num]

            num_Set.add(num)
        return []



if __name__ == '__main__':
    twoSum = TargetSum()
    print('Sub Array of Sum -2 = ', twoSum.twoSumByTwoPointer([0, -1, 2, -3, 1], -2))
    print('Sub Array of Sum 0 = ', twoSum.twoSumByTwoPointer([1, -2, 1, 0, 5], 0))
    print('Sub Array of Sum 16 = ', twoSum.twoSumByTwoPointer([1, 4, 45, 6, 10, -8], 16))

    print('Sub Array of Sum -2 - Hashing Method = ', twoSum.twoSumByHashing([0, -1, 2, -3, 1], -2))
    print('Sub Array of Sum 0 - Hasing Method = ', twoSum.twoSumByHashing([1, -2, 1, 0, 5], 0))
    print('Sub Array of Sum 16 - Hashing Method = ', twoSum.twoSumByHashing([1, 4, 45, 6, 10, -8], 16))

