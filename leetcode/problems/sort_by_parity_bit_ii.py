from typing import List

'''
922. Sort Array By Parity II
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.
'''

def sort_array_by_parity_bit_ii(A: List[int]) -> List[int]:
    odd = [num for num in A if num %2 != 0]
    even = [num for num in A if num %2 == 0]
    i = 0
    for e in even:
        A[i] = e
        i+=2
    i = 1
    for o in odd:
        A[i] = o
        i+=2

    return A

'''
1356. Sort Integers by The Number of 1 Bits
Given an integer array arr. You have to sort the integers in the array in ascending order by the number 
of 1's in their binary representation and in case of two or more integers have the same number of 1's you 
have to sort them in ascending order.
Return the sorted array
'''
