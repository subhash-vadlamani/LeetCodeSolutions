from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance to self is zero
        for i in range(n):
            dist[i][i] = 0
        
        # Add the edges to the distance matrix
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities within the threshold
        min_reachable = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable < min_reachable or (reachable == min_reachable and i > best_city):
                min_reachable = reachable
                best_city = i
        
        return best_city

# Example usage:
# sol = Solution()
# n = 6
# edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
# distanceThreshold = 20
# print(sol.findTheCity(n, edges, distanceThreshold))  # Output should be the index of the city with the smallest number of reachable cities within the distance threshold