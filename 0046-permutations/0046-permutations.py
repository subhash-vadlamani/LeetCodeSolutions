class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        target_length = len(nums)

        # permutation = []
        def dfs(nums, permutation, permutation_length):
            if permutation_length == target_length:
                res.append(permutation.copy())
                return
            
            if not nums:
                return
            
            for num in nums:
                # print(permutation)
                permutation.append(num)
                dfs(nums - {num}, permutation, permutation_length + 1)
                permutation.pop()
        
        dfs(set(nums), [], 0)
        return res
            



        