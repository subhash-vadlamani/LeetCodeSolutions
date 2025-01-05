import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Step1: Create an adj list with the given data

        g = defaultdict(dict)
        for u, v, w in times:
            g[u][v] = w
        
        INF = 10 ** 20
        min_visit_times = [INF] * (n + 1)
        visit_set = set()

        heap = []
        # heap will store a tuple (a, b). a -> time to reach node b

        heapq.heappush(heap, (0, k))
        while heap:
            # break out of the look and return the value if all the nodes have been visited
            if len(visit_set) == n:
                return max(min_visit_times[1:])

            # pop the earliest reachable node
            current_min_time, current_min_time_node = heapq.heappop(heap)

            # update the minimum reachable time for that particular node
            min_visit_times[current_min_time_node] = min(min_visit_times[current_min_time_node], current_min_time)

            
            # explore the node if it has not been already explored
            if current_min_time_node not in visit_set:
                for v, w in g[current_min_time_node].items():
                    heapq.heappush(heap, (current_min_time + w, v))
            
            visit_set.add(current_min_time_node)
        
        # Return -1 if the length of the visit_set is never equal to n

        if len(visit_set) == n:
            return max(min_visit_times[1:])
        else:
            return -1

        