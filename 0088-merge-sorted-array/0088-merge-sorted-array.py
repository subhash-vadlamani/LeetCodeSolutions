class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = 0
        p2 = 0
        current_index = 0

        while(p1 < m or p2 < n):
            if p1 >= m:
                nums1[current_index] = nums2[p2]
                current_index += 1
                p2 += 1
            elif p2 >=n:
                nums1[current_index] = nums1[p1]
                current_index += 1
                p1 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    nums1[current_index] = 
        