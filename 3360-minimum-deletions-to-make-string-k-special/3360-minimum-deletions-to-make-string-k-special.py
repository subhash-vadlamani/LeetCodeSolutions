from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        min_deletions = float('inf')

        for i in range(n):
            # Use freq[i] as the minimum allowed frequency
            base = freq[i]
            deletions = 0
            for f in freq:
                if f < base:
                    deletions += f  # remove all chars with freq < base
                elif f > base + k:
                    deletions += f - (base + k)  # reduce to base + k
            min_deletions = min(min_deletions, deletions)

        return min_deletions
