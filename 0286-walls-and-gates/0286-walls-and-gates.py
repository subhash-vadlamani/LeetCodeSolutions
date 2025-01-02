from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (2 ** 31) - 1
        m = len(rooms)
        n = len(rooms[0])
        
        # Initialize the queue with all gates
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        # Perform BFS from all gates simultaneously
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and rooms[new_i][new_j] == INF:
                    rooms[new_i][new_j] = rooms[i][j] + 1
                    q.append((new_i, new_j))