class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        # compute the dimensions of the grid

        # R-> Number of rows
        # C -> Number of columns

        R = len(grid)
        C = len(grid[0])

        total = 0

        for i in range(R // 2):
            for j in range(C // 2):
                current = 1
                if grid[i][j] == grid[i][C - j - 1]:
                    current += 1
                if grid[i][j] == grid[R - i - 1][j]:
                    current += 1
                if grid[i][j] == grid[R - i - 1][C - j - 1]:
                    current += 1
                
                total += min(current, 4 - current)
        ones = 0
        count = 0
        # if odd number of columns

        if C % 2 == 1:
            for i in range(R // 2):
                if grid[i][C // 2] != grid[R - i - 1][C // 2]:
                    count += 1
            for i in range(R):
                if grid[i][C // 2] == 1:
                    ones += 1
            if C % 2 == 1 and R % 2 == 1 and grid[R // 2][C // 2] == 1:
                ones -= 1

        # if odd number of rows

        if R % 2 == 1:
            for i in range(C // 2):
                if grid[R // 2][i] != grid[R // 2][C - i - 1]:
                    count += 1
            
            for i in range(C):
                if grid[R // 2][i] == 1:
                    ones += 1
            if C % 2 == 1 and R % 2 == 1 and grid[R // 2][C // 2] == 1:
                ones -= 1
        ones %= 4
        total += max(count, min(ones, 4 - ones))

        if C % 2 == 1 and R % 2 == 1 and grid[R // 2][C // 2] == 1:
            total += 1
        return total

        