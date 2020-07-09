from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []

    nums.sort()
    for i in range(0, n):
        if i + 3 > n:
            return result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -1 * nums[i]
        l = i + 1
        r = n - 1
        while l < r:
            actual = nums[l] + nums[r]
            if target == actual:
                result.append([nums[i], nums[l], nums[r]])
                for i in range(l,r):
                    if nums[l] == nums[l+1]:
                        l+=1
                    if nums[r] == nums[r-1]:
                        r-=1
            if actual < target :
                l+=1
            else:
                r-=1
    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0,0,0,0]))
