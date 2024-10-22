class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for s, d, weight in times:
            adj[s].append([d, weight])
        
        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        max_time = float('-inf')

        for i in range(1, n+1):
            if i not in shortest:
                return -1
            current_time = shortest[i]
            if current_time > max_time:
                max_time = current_time
        return max_time
        