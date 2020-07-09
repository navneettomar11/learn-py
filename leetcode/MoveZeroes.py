from typing import List

class MoveZeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1

        for i in range(j, n):
            nums[i] = 0

        print(nums)

if __name__ == '__main__':
    moveZeroes = MoveZeroes()
    moveZeroes.moveZeroes([0,1,0,3,12])

