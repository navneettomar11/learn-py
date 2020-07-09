from typing import List

'''
Sort an array where a subarray of a sorted array is in reverse order
Given an array of N numbers where a subarray is sorted in descending order and rest of the numbers in the array are in ascending order. The task is to sort an array where a subarray of a sorted array is in reversed order.
Input: 2 5 65 55 50 70 90
Output: 2 5 50 55 65 70 90
'''


def sort_array_where_subarray_reversed(nums: List[int]):
    n = len(nums)
    front = -1
    back = -1
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            front = i - 1
            break

    for i in range(n - 2, 0, -1):
        if nums[i] > nums[i + 1]:
            back = i + 1
            break

    if front == -1 and back == -1:
        return

    while front <= back:
        nums[front], nums[back] = nums[back], nums[front]
        front += 1
        back -= 1


'''

Sort an array according to the order defined by another array
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those are in A2. For the elements not present in A2, append them at last in sorted order.

'''


def sort_by_defined_order(nums: List[int], order: List[int]):
    pass  # will be implement latter


'''

Possible to form a triangle from array values
Given an array of integers, we need to find out whether it is possible to construct at least one non-degenerate triangle using array values as its sides. In other words, we need to find out 3 such array indices which can become sides of a non-degenerate triangle.
Examples :

Input : [4, 1, 2]
Output : No 
No triangle is possible from given
array values

Input : [5, 4, 3, 1, 2]
Output : Yes
Sides of possible triangle are 2 3 4

'''


def is_possible_triange(nums: List[int]) -> bool:
    n = len(nums)
    nums.sort()

    for i in range(0, n - 2):
        if nums[i] + nums[i + 1] > nums[i + 2]:
            return True

    return False


'''
Print all triplets in sorted array that form AP
'''
def print_all_triplets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    s = []
    result = []
    for i in range(0, n-1):
        for j in range(i+1, n):
            diff = nums[j] - nums[i]
            if nums[i] - diff in s :
                result.append([nums[i] - diff, nums[i], nums[j]])

        s.append(nums[i])

    return result

'''
'''
