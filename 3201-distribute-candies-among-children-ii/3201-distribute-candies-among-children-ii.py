from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_unbounded_solutions(n):
            return comb(n + 2, 2) if n >= 0 else 0

        total = count_unbounded_solutions(n)

        for over1 in range(3):
            total -= count_unbounded_solutions(n - (limit + 1))

        for over2 in range(3):
            total += count_unbounded_solutions(n - 2 * (limit + 1))

        total -= count_unbounded_solutions(n - 3 * (limit + 1))

        return total
