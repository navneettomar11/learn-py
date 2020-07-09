from typing import List

def plusOne(digits: List[int]) -> List[int]:
    num = int("".join([str(i) for i in digits])) + 1
    return [int(i) for i in str(num)]

if __name__ == "__main__":
    print(plusOne([1,2,3]))
    print(plusOne([4,3,2,1]))
    print(plusOne([9,9,9]))
    print(plusOne([1,9,8,9]))

