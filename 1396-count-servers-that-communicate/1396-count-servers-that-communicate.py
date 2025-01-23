
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = dict()
        col_count = dict()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] = 1 + row_count.get(i, 0)
                    col_count[j] = 1 + col_count.get(j, 0)
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        answer += 1
        return answer

        