class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)

        swaps = 0
        depth = 0
        for c in s:
            if c == "[":
                depth += 1
            elif c == "]":
                if depth > 0:
                    depth -= 1
                else:
                    # swap a "[" from the future
                    depth += 1
                    swaps += 1
        return swaps
                    




        