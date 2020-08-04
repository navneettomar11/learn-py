from typing import List
from collections import Counter
import math


def number_of_steps(num: int) -> int:
    if num < 0:
        return 0

    count = 0
    while num != 0:
        # print(num, 'is Even ', num & 1,' Double ', num >> 1, 'count ', count)
        if num & 1 == 1:
            num -= 1
        else:
            num = num >> 1
        count += 1

    return count


def count_bits(n) -> int:
    count = 0
    while n != 0:
        count += n & 1
        n = n >> 1

    return count


def sort_by_bits(arr: List[int]) -> List[int]:
    num_of_bits_map = dict()
    for num in arr:
        bits = count_bits(num)
        list = num_of_bits_map.get(bits, [])
        list.append(num)
        num_of_bits_map[bits] = list

    bits = [bit for bit in num_of_bits_map.keys()]
    bits.sort()
    res = []
    for bit in bits:
        list = num_of_bits_map[bit]
        list.sort()
        res.extend(list)

    return res


def bitwise_complement(n: int) -> int:
    number_of_bits = (int)(math.floor(math.log(n) /
                                      math.log(2))) + 1
    return ((1 << number_of_bits) - 1) ^ n


def count_prime(num) -> bool:

    primes = [False]*num
    for i in range(2, num):
        primes[i] = True

    i = 2
    while (i*i) < num:
        if primes[i] == True:
            j = i*i
            while j < num:
                primes[j] = False
                j+=i
        i+=1

    count = 0
    for i in range(2, num):
        if primes[i] == True:
            count+=1

    return count

def count_prime_bit_sets(L: int, R: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    return sum(bin(x).count('1') in primes for x in range(L, R + 1))


def has_alteranting_bits(n: int) -> bool:
    binary = [int(n) for n in bin(n)[2:]]
    for i in range(0, len(binary) - 1):
        if binary[i] ^ binary[i + 1] == 0:
            return False

    return True


def missing_numbers(nums: List[int]) -> int:
    n = len(nums)
    sum = n * (n + 1) // 2
    for num in nums:
        sum -= num
    return sum


def find_difference(s: str, t: str) -> str:
    return chr(sum([ord(a) for a in t]) - sum([ord(a) for a in s]))


def is_power_of_four(num: int) -> bool:
    c = 0
    d = 0
    while num > 0:
        if (num & 1) == 1:
            c += 1
        else:
            d += 1
        num = num >> 1
    return c == 1 and d % 2 == 0


def hamming_weight(n: int) -> int:
    c = 0
    while c < n:
        n = n & (n - 1)
        c += 1
    return c


def two_complements(input_value: int, num_bits: int) -> str:
    mask = 2 ** (num_bits - 1)
    return bin((input_value & mask) + (input_value & ~mask))


def majority_element(nums: List[int]) -> int:
    counter = Counter(nums)
    idx = len(nums) // 2
    max_count = max(max(counter.values()), idx)
    for k, v in counter.items():
        if v == max_count:
            return k
    return 0


def two_complement(n: int) -> int:
    num_bytes = math.ceil(n.bit_length() / 8)  # Number required to represent value.
    ba = n.to_bytes(num_bytes, 'big', signed=n < 0)
    return int(''.join('{:08b}'.format(b) for b in ba), 2)


def addition_using_bitoperation(a: int, b: int) -> int:
    def myadd(c, d):
        while d != 0:
            c, d = c ^ d, (c & d) << 1
        return c

    if a < 0 and myadd(~a, 1) <= b or b < 0 and myadd(~b, 1) <= a:
        return ~myadd(myadd(~a, ~b), 1)
    return myadd(a, b)


def subtraction_using_bitoperation(x: int, y: int) -> int:
    a = max(x, y)
    b = min(x, y)
    sign = -1 if x < y else 1
    while (b != 0):
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a * sign


def possible_subset(s: str) -> List[str]:
    n = len(s)
    res = []
    for i in range(0, 1 << n):
        subset = []
        for j in range(0, n):
            if i & (1 << j):
                print('I = ', i, ' J = ', j, 'cond ', (i & (1 << j)), ' s[j] = ', s[j])
                subset.append(s[j])

        res.append(subset)

    return res


def count_bits(n) -> int:
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1

    return count


def read_binary_watch(num: int) -> List[int]:
    res = []
    bit_count_map = {}
    hrlambda = lambda h: h < 12
    for i in range(0, 60):
        bc = count_bits(i)
        l = bit_count_map.get(bc, [])
        l.append(i)
        bit_count_map[bc] = l


    for k, v in bit_count_map.items():
        if k == num:
            res.extend(list(map(lambda h: "{:d}:00".format(h), list(filter( hrlambda, v)))))
            res.extend(list(map(lambda h: "0:{:02d}".format(h), v)))
        elif k < num:
            leftHr = list(filter(hrlambda, v))
            right = bit_count_map.get(num - k, [])
            rightHr = list(filter(hrlambda, right))
            for h in leftHr:
                res.extend(["{:d}:{:02d}".format(h,m) for m in right])
            for h in rightHr:
                res.extend(["{:d}:{:02d}".format(h,m) for m in v])

    return list(sorted(set(res)))


def single_number_ii(nums: List[int]):

   ones = 0
   twos = 0
   for num in nums:
       twos = twos | (ones & num)
       ones = ones ^ num
       not_threes = ~(ones & twos)
       ones = ones & not_threes
       twos = twos & not_threes

   return ones

if __name__ == "__main__":

    print(count_prime(10))
    #print(single_number_ii([2,2,3,2])) # 3
    #print(single_number_ii([0,1,0,1,0,1,99]))
    #print(read_binary_watch(6))

    # print(possible_subset('abc'))
    # print(addition_using_bitoperation(-2,3))
    # print(addition_using_bitoperation(200,23))

    # print(subtraction_using_bitoperation(2,3))
    # print(subtraction_using_bitoperation(200,23))

    # print(number_of_steps(14)) #output - 6
    # print(number_of_steps(8)) #output - 4
    # print(number_of_steps(123)) #output - 12
    # print(number_of_steps(100)) #output - 9
    # print(count_bits(3)) # 2
    # print(count_bits(7)) # 3

    # print(sort_by_bits([0,1,2,3,4,5,6,7,8]))
    # print(sort_by_bits([1024,512,256,128,64,32,16,8,4,2,1]))
    # print(sort_by_bits([10000,10000]))
    # print(sort_by_bits([2,3,5,7,11,13,17,19]))
    # print(sort_by_bits([10,100,1000,10000]))

    # print(bitwise_complement(5)) #output 2

    # print(count_prime_bit_sets(6,10))
    # print(count_prime_bit_sets(10,15))
    # print(count_prime_bit_sets(15,10))
    # print(count_prime_bit_sets(1,10))

    # print(has_alteranting_bits(5))
    # print(has_alteranting_bits(7))
    # print(has_alteranting_bits(10))
    # print(has_alteranting_bits(11))
    # print(has_alteranting_bits(15))
    # print(has_alteranting_bits(21))

    # print(missing_numbers([3,0,1]))
    # print(missing_numbers([9,6,4,2,3,5,7,0,1]))
    # print(find_difference('abcd', 'abcde'))

    # print(is_power_of_four(16)) # True
    # print(is_power_of_four(5)) # false
    # print(is_power_of_four(-5)) # false
    # print(is_power_of_four(2)) # True

    # print(majority_element([3,2,3]))
    # print(majority_element([2,2,1,1,1,2,2]))
