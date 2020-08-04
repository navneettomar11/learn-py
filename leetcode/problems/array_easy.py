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

def decompress_run_list_encode_list(nums: List[int]) -> List[int]:
    n = len(nums)
    if n % 2 != 0:
        return None

    result = []

    for i in range(0, n, 2):
        freq = nums[i]
        val = nums[i+1]
        result.extend([val]*freq)

    return result

def number_identical_pairs(nums: List[int]):
    map = {}
    for num in nums:
        count = map.get(num, 0)
        map[num] = count + 1

    count = 0
    for num in map.keys():
        n = map[num]
        count+=  (n * (n-1))//2

    return count

def is_one_bit_character(bits: List[int])->bool:
    if len(bits) <= 1: return True
    if len(bits) == 2:
        if bits[0] == 1: return False
    one = {}
    res = 0
    twobits = 0 # twobits is a helper variable to count the number of two bits
    for i, bit in enumerate(bits[:-1]):
        print(bit,'--- ', i, len(one))
        if bit == 1 or len(one) == 1:
            one[i] = bit
            twobits += 1
            if twobits == 2:
                res += 2
                one.clear()
                twobits = 0
        else:
            res += 1
    if len(bits) - res == 1:
        return True
    else:
        return False

def gray_code(n: int)->List[int]:
    return [int(i ^ ( i >> 1)) for i in range(0, pow(2, n))]

def mypow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1/x * mypow(1/x, -(n+1))
    if n%2 != 0:
        return x * mypow(x*x, n//2)

    return mypow(x*x,n//2)

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    map = {}
    n = len(nums)
    bucket = [ [] for i in range(0, n+1)]

    for num in nums:
        map[num] = map.get(num, 0) + 1

    for num,c in map.items():
        bucket[c].append(num)

    res = []*k
    for i in range(n, 0, -1):
        if len(bucket[i]) > 0 :
            res.extend(bucket[i])
        if len(res) == k:
            break

    return res


def remove_duplicates(nums: List[int]) -> List[int] :
    idx = 0
    while idx < len(nums):
        jdx = idx
        while jdx < len(nums) - 1 and nums[jdx] == nums[jdx + 1]:
            #print(idx, jdx, len(nums),'----', nums[idx], nums[jdx])
            nums.pop(jdx)
        idx+=1

    return nums

def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    end = len(numbers) - 1
    start = 0
    while start != end:
        sum = numbers[start]+numbers[end]
        if sum == target:
            return [start+1, end+1]
        elif sum < target:
            start+=1
        else:
            end-=1

    return []

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    jdx = 0
    start_idx = 0
    nums1.sort()
    nums2.sort()

    for idx in range(len(nums1)):
        while jdx < len(nums2):
            if nums1[idx] == nums2[jdx]:
                start_idx = jdx+1
                res.append(nums1[idx])
                break;
            jdx+=1

        jdx = start_idx
    return res


def height_checker(heights: List[int]) -> int :
    sorted_heights = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count+=1

    return count

def rotate_array(nums: List[int], k: int):
    def reverse_helper(nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    n = len(nums)
    k%= n
    reverse_helper(nums, 0, n-1)
    reverse_helper(nums, 0, k-1)
    reverse_helper(nums, k, n-1)

def contains_duplicate(nums: List[int]) -> bool:
    return not(len(set(nums)) == len(nums))

def single_number(nums: List[int]) -> int:
    n = 0
    for num in nums:
        n=num ^ n

    return n


def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    map = {}
    for i in range(n):
        #print(map, nums[i])
        diff = target - nums[i]
        if map.get(nums[i]) is not None:
            return [map.get(nums[i]), i]

        map[diff] = i

    return []

def reverse_int(x: int) -> int:
    if x >= 2**31-1 or x <= -2**31: return 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = []
    p = 0
    while x > 0:
        res.append(x % 10)
        x//=10
        p+=1

    n = len(res)
    r = 0
    for i in range(n):
        r+= pow(10, n-1-i)*res[i]

    return r

def single_number(nums: List[int]) -> List[int]:
    num_map =  {}
    for num in nums:
        count = num_map.get(num, 0)
        num_map[num] = count + 1

    return list(dict(filter(lambda elem: elem[1] == 1, num_map.items())).keys())


def find_minimum_element( nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return -1

    for i in range(1,n):
        if nums[i-1] > nums[i]:
            return nums[i]

    return nums[0]

def majority_element(nums: List[int]) -> int:
    num_count_map = {}
    for num in nums:
        count = num_count_map.get(num, 0)
        num_count_map[num] = count + 1

    mid = len(nums)//2
    print(num_count_map, mid)



def climbing_stairs(n: int) -> int:
    def count_stair(n):
        if n <= 1:
            return n
        return count_stair(n-1) + count_stair(n-2)

    return count_stair(n+1)


def shift_array(arr: List[int], start: int, num: int) -> List[int]:
    temp = []
    temp.extend(arr[0:start])
    temp.append(num)
    temp.extend(arr[start:])
    return temp

def create_target_array(nums: List[int], index: List[int]) -> List[int]:
    target = []
    for i in range(0,len(nums)):
        target = target[0:index[i]] + [nums[i]] + target[index[i]:]
    return target


def odd_cells(n: int, m: int, indices: List[List[int]]):
    matrix = [ [0]*m for i in range(0,n)]
    ll = len(indices)
    for i in range(0,ll):
        row = indices[i][0]
        col = indices[i][1]
        for c in range(0,m):
            matrix[row][c]+=1
        for r in range(0,n):
            matrix[r][col]+=1

    count = 0
    for r in range(0, n):
        for c in range(0,m):
            count+= 1 if matrix[r][c] & 1 == 1 else 0

    return count

def add_to_array_form(A: List[int], K: int) -> List[int]:
    return [int(c) for c in str(int(''.join([str(c) for c in A])) + K)]

def array_pair_sum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[::2])


def average_salary(salary: List[int]) -> int:
    n = len(salary)
    return (sum(salary) - min(salary) - max(salary))/(n-2)

if __name__ == "__main__":

    print(average_salary([4000,3000,1000,2000]))
    #print(array_pair_sum([1,4,3,2])) # 4
    #print(array_pair_sum([-7,5,-6,8])) # 12
    #print(add_to_array_form([1,2,0,0], 34))
    #print(odd_cells(2,3,[[0,1], [1,1]])) # 6
    #print(odd_cells(2,2,[[1,1], [0,0]])) # 0
    #print(create_target_array([0,1,2,3,4], [0,1,2,2,1]))
    #print(create_target_array([1,2,3,4,0], [0,1,2,3,0]))
    #print(decompress_run_list_encode_list([1,2,3,4]))
    #print(decompress_run_list_encode_list([1,1,2,3]))
    #print(decompress_run_list_encode_list([0,1,2,3]))
    #print(number_identical_pairs([1,2,3,1,1,3]))
    #print(number_identical_pairs([1,1,1,1]))
    #print(number_identical_pairs([1,2,3]))

    #print(is_one_bit_character([1, 1, 1, 1,0,0]))
    #print(mypow(3.00000,-3))
    #print(gray_code(2))
    #print(gray_code(0))

    #print(top_k_frequent([1,1,1,2,2,3], 2)) # [1,2]
    #print(top_k_frequent([1], 1)) # [1]
    #print(top_k_frequent([1,2,2,3,3], 2)) # [2,3]
    #print(top_k_frequent([3,0,1,0], 1)) # [0]

    #print(remove_duplicates([1,1,2])) # [1,2]
    #print(remove_duplicates([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4]
    #print(remove_duplicates([-1,0,1,1,2,9,9])) # [-1,0,1,2,9]
    #print(remove_duplicates([-10,1,3,6,6,6,6,10])) #[-10,1,3,6,10]

    #print(two_sum_ii([2,7,11,15], 9))

    #print(intersect([1,2,2,1], [2,2])) #[2,2]
    #print(intersect([4,9,5], [9,4,9,8,4])) #[4,9]
    #print(intersect([1,2], [1,1])) #[1]
    #print(intersect([3,1,2], [1,1])) #[1]
    #print(intersect([1,2,2,1], [2])) #[2]

    #print(height_checker([1,1,4,2,1,3])) # 3
    #print(height_checker([5,1,2,3,4])) #5
    #print(height_checker([1,2,3,4,5])) #0

    #print(contains_duplicate([1,2,3,1]))
    #print(contains_duplicate([1,2,3,4]))

    #print(single_number([2,2,1]))
    #print(single_number([4,1,2,1,2]))

    #print(two_sum([2, 7, 11, 15], 9))
    #print(reverse_int(123)) # output - 321
    #print(reverse_int(1534236469)) # output - 0

    #print(single_number([1,2,1,3,2,5])) #output - [3,5]
    #print(single_number([1,2])) #output - [1,2]
    #print(single_number([1,2,4,0,9])) #output - [0,1,2,4,9]

    #print(find_minimum_element([3,4,5,1,2])) # output 1
    #print(find_minimum_element([4,5,6,7,0,1,2])) # output = 0
    #print(find_minimum_element([])) # output = -1
    #print(find_minimum_element([2,3,1])) # output = 1
    #print(find_minimum_element([3,1])) # output = 1
    #print(find_minimum_element([4,5,1,2,3])) # output = 1
    #print(find_minimum_element([2,2,2,0,1])) #output = 0
    #print(find_minimum_element([3,3,1,3])) #output = 1

    #print(majority_element([3,2,3])) #output = 3
    #print(climbing_stairs(1)) #output = 1
    #print(climbing_stairs(2)) #output = 2
    #print(climbing_stairs(3)) #output = 3
    #print(climbing_stairs(4)) #output = 5
