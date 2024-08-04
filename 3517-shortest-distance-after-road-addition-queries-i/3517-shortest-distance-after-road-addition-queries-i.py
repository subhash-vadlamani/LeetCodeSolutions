import heapq
from collections import defaultdict
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def dijkstra(g, n, s, e):
            vis = [False] * n
            MAX = 10 ** 20
            dist = [MAX] * n
            dist[s] = 0

            pq = [(0, s)]

            while pq:
                current_distance, current_vertex = heapq.heappop(pq)
                vis[current_vertex] = True
                if dist[current_vertex] < current_distance:
                    continue
                
                for node in g[current_vertex]:
                    if vis[node]:
                        continue
                    new_dist = dist[current_vertex] + 1
                    if new_dist < dist[node]:
                        dist[node] = new_dist
                        heapq.heappush(pq, (new_dist, node))
            return dist[e]

        
        graph = defaultdict(dict)

        for i in range(n-1):
            graph[i][i+1] = 1
        answer_list = []

        for query in queries:
            start_node = query[0]
            end_node = query[1]

            graph[start_node][end_node] = 1

            current_answer = dijkstra(graph, n,  0, n - 1)
            answer_list.append(current_answer)
        return answer_list
        



        