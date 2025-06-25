class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        DFS with memoization
        at each point, either insert, delete or replace

        """

        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # def get_nei_max(i, j):
        #     # Get the maximum of the neighbour cells if they are in range, else 0
        #     directions = [(1, 0), (0, 1)]
        #     current_max = 0
        #     for di, dj in directions:
        #         new_i, new_j = i + di, j + dj
        #         if new_i in range(m) and new_j in range(n):
        #             current_max = max(current_max, dp[new_i][new_j])
        #     return current_max


        # Bottom Up Approach
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if word1[i] == word2[j]:
        #             dp[i][j] = 1 + dp[i+1][j + 1]
        #         else:
        #             dp[i][j] = min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        # return dp[0][0]
        
        memo = {}
        if m == 0 and n == 0:
            return 0
        elif m == 0:
            return n
        elif n == 0:
            return m

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                answer =  dfs(i+1, j+1)
            
            else:
                # 3 options
                answer =  1 + min(dfs(i+1, j+1), dfs(i, j+1), dfs(i+1, j))
            
            memo[(i, j)] = answer
            return answer
        
        return dfs(0, 0)

