from typing import List

def can_jump(nums: List[int]) -> bool :
    n =  len(nums)
    if n == 1:
        return  True

    last_jump = n - 1

    for i in range(n-1, -1, -1):
        print(nums[i], i)
        if i + nums[i] >= last_jump:
            last_jump = i

    return  last_jump == 0


if __name__ == "__main__":
    print(can_jump([2,3,1,1,4]))
    print(can_jump([3,2,1,0,4]))
    print(can_jump([2,3,4,5,1]))

