class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        N = len(nums)

        for _ in range(N):
            for j in range(N-1, 0, -1):
                if nums[j] < nums[j-1] and nums[j].bit_count() == nums[j-1].bit_count():
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                
        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True