from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        # dist[i][j] = best‐known earliest arrival at (i,j)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]           # (time, i, j)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            time, i, j = heapq.heappop(heap)
            if time > dist[i][j]:
                continue
            # once we pop the target, it's the minimum possible
            if i == n-1 and j == m-1:
                return time

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    arrive = max(time, moveTime[ni][nj]) + 1
                    if arrive < dist[ni][nj]:
                        dist[ni][nj] = arrive
                        heapq.heappush(heap, (arrive, ni, nj))

        return -1  # unreachable (by problem constraints this shouldn't happen)
