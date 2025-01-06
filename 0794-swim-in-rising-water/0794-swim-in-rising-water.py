import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visit = set()
        minHeap = [[grid[0][0], (0, 0)]] # [elevation, point]
        t = 0
        while minHeap:
            # Increment the t until the level of water is enough to pop the lowest grid element
            while t < minHeap[0][0]:
                t += 1
            _, (i, j) = heapq.heappop(minHeap)
            if (i, j) in visit:
                continue
            
            visit.add((i, j))
            if (n - 1, n - 1) in visit:
                return t
            # Explore the neighbours of (i, j)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if new_i in range(n) and new_j in range(n):
                    heapq.heappush(minHeap, [grid[new_i][new_j], (new_i, new_j)])
        return t
            



        