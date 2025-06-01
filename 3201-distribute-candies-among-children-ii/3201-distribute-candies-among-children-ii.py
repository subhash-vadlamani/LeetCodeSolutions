class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        total = 0

        for i in range(min(n, limit) + 1):
            candies_left = n - i

            if limit >= candies_left:
                total += candies_left + 1
            else:
                total += max(limit - (candies_left - limit) + 1, 0)
        
        return total
        