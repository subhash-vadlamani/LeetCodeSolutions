from collections import deque, defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def parity_counts(n: int, edges: List[List[int]]):
            """
            Build the tree on n nodes, BFS from 0 to compute:
              - depth[i] = distance from 0
              - cnt_even = # nodes at even depth
              - cnt_odd  = # nodes at odd depth
            Returns depth array, cnt_even, cnt_odd.
            """
            g = defaultdict(list)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            depth = [-1]*n
            dq = deque([0])
            depth[0] = 0
            cnt_even = 1
            cnt_odd  = 0

            while dq:
                u = dq.popleft()
                for w in g[u]:
                    if depth[w] == -1:
                        depth[w] = depth[u] + 1
                        if depth[w] & 1:
                            cnt_odd += 1
                        else:
                            cnt_even += 1
                        dq.append(w)

            return depth, cnt_even, cnt_odd

        # --- process tree2 to get its max “odd‐distance” count (since
        #     the original used is_even_required=False → count nodes at odd dist) 
        m = len(edges2) + 1
        depth2, even2, odd2 = parity_counts(m, edges2)
        graph2_max = max(odd2, even2)  # whichever parity gives more targets

        # --- process tree1 to get per-node “even‐distance” counts by parity flip—
        #     we only ever need the “even‐distance” count from each node,
        #     and that is either even1 or odd1 depending on its depth‐parity.
        n = len(edges1) + 1
        depth1, even1, odd1 = parity_counts(n, edges1)

        # build answer in O(n)
        ans = []
        for i in range(n):
            # if i is at even depth from 0, its “even‐distance” count = even1,
            # otherwise = odd1  (because shifting root across each edge flips parity)
            base = even1 if (depth1[i] % 2 == 0) else odd1
            ans.append(base + graph2_max)

        return ans
