class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            wherever the rotation index is, that is the minimum element
        """

        def find_index(nums):
            l = 0
            r = len(nums) - 1

            while l < r:
                mid = (l + r) // 2

                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        required_index = find_index(nums)
        return nums[required_index]

        