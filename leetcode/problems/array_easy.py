from typing import List

def shuffle_array(nums: List[int], n: int) -> List[int] :
    l = len(nums)

    if l < n:
        return nums

    result = []

    for i in range(0,n):
        result.append(nums[i])
        result.append(nums[i+n])

    return result

def kid_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandy = max(candies)
    return  [(candy + extraCandies) >= maxCandy for candy in candies]

def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    temp = sorted(nums)
    return [(temp.index(num)) for num in nums ]

