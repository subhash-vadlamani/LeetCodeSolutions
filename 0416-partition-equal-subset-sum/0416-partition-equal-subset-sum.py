class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        """
            Sum of all the elements should be divisible by 2 for this to be possible
        """

        total_sum = sum(nums)
        N = len(nums)
        if total_sum % 2 == 1:
            return False
        
        cache = {}
        
        """
            2 choices for each element. either be in subset 1 or subset 2
        """

        def compute_subsets(subset1, subset1_sum, subset2, subset2_sum, index):

            """
                base case 1: 
                the subset1 sum is equal to total_sum//2
            """
            if f"{subset1_sum}, {subset2_sum}, {index}" in cache:
                return cache[f"{subset1_sum}, {subset2_sum}, {index}"]

            if subset1_sum > total_sum // 2 or subset2_sum > total_sum // 2:
                return False
            
            if (subset1_sum == total_sum // 2 or subset2_sum == total_sum // 2) and index == N:
                return True
            
            answer =  (compute_subsets(subset1 + [nums[index]], subset1_sum + nums[index], subset2, subset2_sum, index + 1) 
            or compute_subsets(subset1, subset1_sum, subset2 + [nums[index]], subset2_sum + nums[index], index + 1))
            cache[f"{subset1_sum}, {subset2_sum}, {index}"] = answer

            return answer
        
        return compute_subsets([], 0, [], 0, 0)
            

        