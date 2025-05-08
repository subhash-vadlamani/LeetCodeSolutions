import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
            solved through using a min-heap. min-heap keeps the 
            node with the earliest time reached. We can explore that node accordingly.
            The first occurrance of destination, we return the value stored in the heap
        """
        n = len(moveTime)
        m = len(moveTime[0])
        min_heap = [(0, (0, 0))] # (time_to_reach_the_cell, cell_coordinates)
        destination_cell_tuple = (n - 1, m - 1)
        visit = set()
        visit.add((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            current_min_time, current_cell_tuple = heapq.heappop(min_heap)

            if current_cell_tuple == destination_cell_tuple:
                return current_min_time
            
            # visit.add(current_cell_tuple)
            
            for dr, dc in directions:
                new_r = current_cell_tuple[0] + dr
                new_c = current_cell_tuple[1] + dc

                if new_r in range(n) and new_c in range(m) and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    new_cell_time = max(current_min_time, moveTime[new_r][new_c]) + 1
                    heapq.heappush(min_heap, (new_cell_time, (new_r, new_c)))
        
        return -1
            


        