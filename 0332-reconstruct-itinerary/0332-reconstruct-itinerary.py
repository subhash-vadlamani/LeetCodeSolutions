from collections import defaultdict
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        tickets.sort(reverse = True)

        for src, dest in tickets:
            adj[src].append(dest)
        
        res = []

        def dfs(src):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            res.append(src)
        
        dfs("JFK")

        return res[::-1]


        