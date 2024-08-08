class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        seen = set()
        ans = []
        curr = (rStart, cStart)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        jumps_needed = 1
        
        while len(seen) < rows * cols:
            r, c = curr
            for _ in range(jumps_needed):
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in seen:
                    seen.add((r, c))
                    ans.append([r, c])
                dr, dc = DIRECTIONS[curr_dir]
                r += dr
                c += dc
            curr = (r, c)
            curr_dir = (curr_dir + 1) % 4

            if curr_dir == 0 or curr_dir == 2:
                jumps_needed += 1

        return ans 