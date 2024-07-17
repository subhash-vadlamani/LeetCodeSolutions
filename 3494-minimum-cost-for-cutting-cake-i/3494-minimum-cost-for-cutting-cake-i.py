class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        INF = 10 ** 20

        @cache
        def go(ax, ay, bx, by):
            if((ax + 1 == bx) and (ay + 1 == by)):
                return 0
            
            best = INF

            for i in range(ax + 1, bx):
                best = min(best, go(ax, ay, i, by) + go(i, ay, bx, by) + horizontalCut[i-1])
            
            for i in range(ay + 1, by):
                best = min(best, go(ax, ay, bx, i) + go(ax, i, bx, by) + verticalCut[i-1])
            
            return best
        
        return go(0, 0, m, n)
        