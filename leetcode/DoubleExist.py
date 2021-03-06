from typing import List


class DoubleExist:

    def checkIfExist(self, arr: List[int]) -> bool:

        n = len(arr)
        for i in range(0,n):
            r  = arr[i] * 2
            for j in range(0,n):
                if i != j and r == arr[j]:
                    return True
        return False


if __name__ == '__main__':
    dobuleExist = DoubleExist()
    print(dobuleExist.checkIfExist([10,2,5,3]))
    print(dobuleExist.checkIfExist([7,1,14,11]))
    print(dobuleExist.checkIfExist([3,1,7,11]))
    print(dobuleExist.checkIfExist([0,0]))
