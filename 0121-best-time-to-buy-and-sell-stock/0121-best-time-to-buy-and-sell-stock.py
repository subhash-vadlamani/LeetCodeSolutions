class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price < min_so_far:
                min_so_far = current_price
            else:
                current_profit = current_price - min_so_far
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit

        