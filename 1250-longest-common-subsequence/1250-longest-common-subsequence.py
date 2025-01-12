class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        def get_nei_max(i, j):
            # Get the maximum of the neighbour cells if they are in range, else 0
            directions = [(1, 0), (0, 1)]
            current_max = 0
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if new_i in range(m) and new_j in range(n):
                    current_max = max(current_max, dp[new_i][new_j])
            return current_max


        # Bottom Up Approach
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    if (i + 1) in range(m) and (j + 1) in range(n):
                        dp[i][j] = 1 + dp[i+1][j + 1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = get_nei_max(i, j)
        return dp[0][0]


        