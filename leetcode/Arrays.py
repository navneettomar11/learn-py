from typing import  List
class Arrays:

    def __init__(self):

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx]*=-1

        print(nums)

        for i in range(0,len(nums)):
            if nums[i] > 0:
                ret.append(i+1)

        return ret

if __name__ == '__main__':
    arrays = Arrays()
    print(arrays.findDisappearedNumbers([4,3,2,7,8,2,3,1])) # [5,6]
    print(arrays.findDisappearedNumbers([1,1])) # [2]
