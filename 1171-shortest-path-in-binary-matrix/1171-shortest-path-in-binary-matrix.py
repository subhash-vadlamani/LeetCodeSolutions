from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the start or end is blocked
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        n = len(grid)
        
        # Directions for 8-directional movement
        directions = [
            (1, 0), (1, 1), (0, 1), (-1, 1),
            (-1, 0), (-1, -1), (0, -1), (1, -1)
        ]
        
        # Initialize the queue for BFS
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark the starting cell as visited
        
        while queue:
            r, c, length = queue.popleft()
            
            # If we have reached the bottom-right cell
            if r == n - 1 and c == n - 1:
                return length
            
            # Check all 8 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, length + 1))
                    grid[nr][nc] = 1  # Mark the cell as visited
        
        # If there is no clear path
        return -1