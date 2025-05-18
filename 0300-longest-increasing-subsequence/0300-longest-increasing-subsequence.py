class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        nums_len = len(nums)
        lis = [1] * nums_len

        for i in range(nums_len):
            for j in range(i):
                if (nums[i] > nums[j]) and (lis[j] + 1 > lis[i]):
                    lis[i] = lis[j] + 1
        
        return max(lis)
        