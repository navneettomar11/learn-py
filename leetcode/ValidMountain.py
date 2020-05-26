from typing import  List

class ValidMountain:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)

        if n < 3:
            return False

        point = -1
        for i in range(n-1):
            if A[i] >= A[i+1]:
                point = i
                break
        if point > 0:
            for i in range(point, n-1):
                if A[i] <= A[i+1]:
                    return False
            return True

        return False


if __name__ == '__main__':
    validMountain = ValidMountain()
    print(validMountain.validMountainArray([2,1]))
    print(validMountain.validMountainArray([3,5,5]))
    print(validMountain.validMountainArray([0,3,2,1]))
    print(validMountain.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
    print(validMountain.validMountainArray([9,8,7,6,5,4,3,2,1,0]))
