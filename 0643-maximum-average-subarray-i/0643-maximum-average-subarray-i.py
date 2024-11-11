class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == k:
            return round(sum(nums) / k, 5)
        
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        max_sum = current_sum
        l = 0
        r = k 

        while r < n:
            current_sum += nums[r]
            current_sum -= nums[l]
            l += 1
            r += 1
            if current_sum > max_sum:
                max_sum = current_sum
        return round(max_sum / k, 5)
        

        