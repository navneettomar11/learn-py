from typing import List
from .InsertionSort import InsertionSort

class BucketSort:

    def __init__(self) -> None:
        self.insertion_sort = InsertionSort()

    """Normal Sort"""
    def sort(self, nums: List[float]):
        n = len(nums)
        buckets = []
        for i in range(n):
            buckets.append([])

        for num in nums:
            index = int(n * num)
            buckets[index].append(num)

        for i in range(n):
            self.insertion_sort.sort(buckets[i])

        k = 0
        for i in range(n):
            for j in range(len(buckets[i])):
                nums[k] = buckets[i][j]
                k+=1

    '''
    Bucket Sort To Sort an Array with Negative Numbers
    :param nums
    :return None
    '''
    def sort_with_negative_numbers(self, nums: List[float]):
        n = len(nums)
        negative_nums = [-1 * num for num in nums if num < 0]
        postive_nums = [ num for num in nums if num >= 0]

        self.sort(negative_nums)
        self.sort(postive_nums)

        k = 0
        for num in negative_nums:
            nums[k] = -1 * num
            k+=1

        for num in postive_nums:
            nums[k] = num
            k+=1

