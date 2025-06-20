class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        N = len(s)

        directions = [
            (1, 0), # E
            (0, 1), # S
            (-1, 0), # W
            (0, -1) # N
        ]

        ds = "ESWN"
        counts = [0] * 4
        best = 0

        for c in s:
            d = ds.index(c)
            counts[d] += 1
            
            mxx = max(counts[0], counts[2])
            mnx = min(counts[0], counts[2])

            ck = k
            used = min(mnx, ck)
            mnx -= used
            ck -= used
            mxx += used

            mxy = max(counts[1], counts[3])
            mny = min(counts[1], counts[3])

            used = min(mny, ck)
            mny -= used
            ck -= used
            mxy += used

            best = max(best, mxx - mnx + mxy - mny)

            # best = max(best, abs(counts[0] - counts[2]) + abs(counts[1] - counts[3]))
        return best