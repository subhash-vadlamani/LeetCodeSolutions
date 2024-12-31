from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = set()

        def bfs(r, c):
            q = deque()

            q.append((r, c))
            visited.add((r, c))

            while q:
                x, y = q.popleft()

                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for dr, dc in directions:
                    r1 = x + dr
                    c1 = y + dc

                    if r1 in range(m) and c1 in range(n) and grid[r1][c1] == "1" and (r1, c1) not in visited:
                        q.append((r1, c1))
                        visited.add((r1, c1))
        
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)

                    island_count += 1
        return island_count


        