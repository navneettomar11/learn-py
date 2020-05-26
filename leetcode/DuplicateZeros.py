from typing import List


class DuplicateZeros:

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
    duplicateZeros = DuplicateZeros()
    arr = [1,0,2,3,0,4,5,0]
    duplicateZeros.duplicateZeros(arr)
    print(arr)
    arr = [1,2,3]
    duplicateZeros.duplicateZeros(arr)
    print(arr)
