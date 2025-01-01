from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = set()

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited.add((r, c))

            current_area = 1

            while q:
                r, c = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r1 = r + dr
                    c1 = c + dc

                    if r1 in range(m) and c1 in range(n) and grid[r1][c1] == 1 and (r1, c1) not in visited:
                        current_area += 1
                        q.append((r1, c1))
                        visited.add((r1, c1))
            return current_area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    current_area = bfs(i, j)
                    max_area = max(max_area, current_area)
        
        return max_area

        