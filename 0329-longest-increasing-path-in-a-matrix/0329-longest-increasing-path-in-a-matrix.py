class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]  # -1 = not visited

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            max_path = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))

            memo[i][j] = max_path
            return max_path

        return max(dfs(i, j) for i in range(m) for j in range(n))
