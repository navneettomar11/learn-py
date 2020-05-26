from typing import List


class MergeSortedArray:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = []

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    MergeSortedArray().merge(nums1, 3, [2,5,6], 3)
    print(nums1)

