class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        new_grid = [[0 for _ in range(n*3)] for __ in range(m*3)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "/":
                    for k in range(3):
                        new_grid[(i*3)+k][(j*3)+(2-k)] = 1
                if grid[i][j] == "\\":
                    for k in range(3):
                        new_grid[(i*3)+k][(j*3)+k] = 1
        DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(new_grid)
        n = len(new_grid[0])
        def clear_grid(r,c):
            new_grid[r][c] = 1
            for dr,dc in DIRECTIONS:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < m and 0 <= nc < n and new_grid[nr][nc] == 0:
                    clear_grid(nr,nc)
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if new_grid[i][j] == 0:
                    num_islands += 1
                    clear_grid(i,j)
        return num_islands
