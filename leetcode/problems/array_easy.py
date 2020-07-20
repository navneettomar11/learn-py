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
            print(idx, jdx, len(nums),'----', nums[idx], nums[jdx])
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

if __name__ == "__main__":
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

    print(intersect([1,2,2,1], [2,2])) #[2,2]
    print(intersect([4,9,5], [9,4,9,8,4])) #[4,9]
    print(intersect([1,2], [1,1])) #[1]
    print(intersect([3,1,2], [1,1])) #[1]
    print(intersect([1,2,2,1], [2])) #[2]
