class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        VALID_NUMS = set([1,2,3,4,5,6,7,8,9])
        def is_magic_square(sub_grid):
            seen = set()
            # Has valid rows
            target_sum = sum(sub_grid[0])
            for row in sub_grid:
                if sum(row) != target_sum:
                    return False
            # Has valid columns
            for i in range(len(sub_grid)):
                curr_col = []
                for j in range(len(sub_grid[0])):
                    num = sub_grid[j][i]
                    if num in seen:
                        return False
                    seen.add(num)
                    if num not in VALID_NUMS:
                        return False
                    curr_col.append(num)
                if sum(curr_col) != target_sum:
                    return False
            # Has Valid Diagonals
            t = sub_grid[0][0] + sub_grid[1][1] + sub_grid[2][2]
            if t != target_sum:
                return False
            t = sub_grid[2][0] + sub_grid[1][1] + sub_grid[0][2]
            if t != target_sum:
                return False
            return True
                
        ans = 0
        for k in range(2,m):
            for kk in range(2,n):
                sub_grid = []
                for i in range(k-2,k+1):
                    flag = True 
                    curr_row = []
                    for j in range(kk-2,kk+1):
                        num = grid[i][j]
                        curr_row.append(num)
                    sub_grid.append(curr_row) 
                if is_magic_square(sub_grid):
                    ans += 1
        return ans
