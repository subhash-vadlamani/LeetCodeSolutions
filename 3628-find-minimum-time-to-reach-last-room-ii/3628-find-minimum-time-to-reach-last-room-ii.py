import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        
        # (time, row, col, parity), where parity: 0 (even move), 1 (odd move)
        min_heap = [(0, 0, 0, 0)]  # start at (0,0), time=0, 0 steps taken
        min_time_required = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        min_time_required[0][0][0] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            time, r, c, parity = heapq.heappop(min_heap)

            if (r, c) == (n - 1, m - 1):
                return time

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < m:
                    next_parity = 1 - parity
                    move_cost = 1 if parity == 0 else 2
                    wait_time = max(time, moveTime[new_r][new_c])
                    next_time = wait_time + move_cost

                    if next_time < min_time_required[new_r][new_c][next_parity]:
                        min_time_required[new_r][new_c][next_parity] = next_time
                        heapq.heappush(min_heap, (next_time, new_r, new_c, next_parity))

        return -1  # unreachable
