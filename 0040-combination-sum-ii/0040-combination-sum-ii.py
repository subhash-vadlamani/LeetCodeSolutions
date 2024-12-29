class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def dfs(index, current_list, current_sum):
            if current_sum == target:
                res.append(current_list.copy())
                return
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                current_list.append(candidates[i])
                dfs(i + 1, current_list, current_sum + candidates[i])
                current_list.pop()
        dfs(0, [], 0)
        return res