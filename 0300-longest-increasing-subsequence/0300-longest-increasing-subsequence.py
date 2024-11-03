class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        lis = [1] * N

        for i in range(N-2, -1, -1):
            current_lis = 1
            # current_value = nums[i]

            for j in range(i+1, N):
                if nums[j] > nums[i]:
                    current_lis = max(current_lis, 1 + lis[j])
            lis[i] = current_lis
        
        return max(lis)
        