from typing import List


class DuplicateZeros:

    def shiftArrayToRight(self, arr: List[int], start: int, end: int):
        i = start
        while i < end:
            arr[i+1] = arr[i]

    def duplicateZeros(self, arr: List[int]):
            n = len(arr)
            skip = False
            for i in range(n):
                if arr[i] == 0 and skip == False:
                    arr.insert(i,0)
                    arr.pop()
                    skip = True
                else: skip = False


if __name__ == '__main__':
    arr = [1,0,2,3,0,4,5,0]
    DuplicateZeros().duplicateZeros(arr)
    print(arr)
    arr = [1,2,3]
    DuplicateZeros().duplicateZeros(arr)
    print(arr)
