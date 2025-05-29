from collections import deque

class Solution:
    def BFS(self, start, adj, k):
        q = deque()
        q.append((start, -1))
        count = 0

        while q and k >= 0:
            size = len(q)
            count += size
            for _ in range(size):
                u, parent = q.popleft()
                for v in adj[u]:
                    if v != parent:
                        q.append((v, u))
            k -= 1
        return count

    def maxTargetNodes(self, edges1, edges2, k):
        m = len(edges1) + 1
        n = len(edges2) + 1

        # Build adjacency lists for tree 1
        adj1 = [[] for _ in range(m)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        # Build adjacency lists for tree 2
        adj2 = [[] for _ in range(n)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Preprocess: Find the best node in Tree-2
        best = 0
        for i in range(n):
            connections = self.BFS(i, adj2, k - 1)
            best = max(best, connections)

        # Build answer
        res = []
        for i in range(m):
            connections = self.BFS(i, adj1, k)
            res.append(connections + best)
        return res