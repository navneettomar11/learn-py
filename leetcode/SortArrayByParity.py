from typing import List

class SortArrayByParity:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        temp = []
        for i in range(0, n):
            if A[i] % 2 == 0:
                temp.append(A[i])

        for i in range(0, n):
            if A[i] % 2 != 0:
                temp.append(A[i])

        return temp


    def foo(self, arr: List[int]):
        temp = [i+1 for i in arr]
        print(temp)

if __name__ == "__main__":
    sortArrayByParity = SortArrayByParity()
    print(sortArrayByParity.sortArrayByParity([3,1,2,4])) # [2,4,3,1]
    sortArrayByParity.foo([1,2,3,4])
