class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Code Credits -> LarryNY
        INF = 10 ** 20
        events.sort()

        best_previous = -INF
        best = max(v for _, _, v in events)

        h = []
        for s, e, v in events:
            # Our current sweepline is at "s"
            # We want to process all the previous "endings" from before
            while len(h) > 0 and h[0][0] < s:
                _, nv = heapq.heappop(h)
                best_previous = max(best_previous, nv)
            heapq.heappush(h, (e, v))
            best = max(best, best_previous + v)
        return best
        