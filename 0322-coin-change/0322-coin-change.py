class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            min_coins = -1
            for c in coins:
                remaining_amount = a - c
                if remaining_amount < 0 or dp[remaining_amount] == -1:
                    continue
                
                if min_coins == -1:
                    min_coins = 1 + dp[remaining_amount]
                else:
                    min_coins = min(min_coins, 1 + dp[remaining_amount])
            dp[a] = min_coins
        
        return dp[amount]
                
        