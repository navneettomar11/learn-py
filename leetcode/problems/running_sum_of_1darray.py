from typing import List

def running_sum(nums: List[int]) -> List[int]:
   s = 0
   result = []
   for num in nums:
       s+=num
       result.append(s)
   return result

def xor_operations(n: int, start: int) -> int:
    result = 0
    for i in range(0, n):
        result = result ^ start + 2*i

    return result
