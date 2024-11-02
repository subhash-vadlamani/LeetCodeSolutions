class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minimum_coins_list = [-2] * (amount + 1)
        minimum_coins_list[0] = 0

        def compute_minimum_coins(amount):

            if amount < 0:
                return -1

            if minimum_coins_list[amount] != -2:
                return minimum_coins_list[amount]
            
            current_min = -1
            for coin in coins:
                remaining_amount = amount - coin
                if remaining_amount < 0 or minimum_coins_list[remaining_amount] == -1:
                    continue
                
                current_coins = 1 + compute_minimum_coins(remaining_amount)
                if current_coins == 0:
                    continue
                
                if current_min == -1:
                    current_min = current_coins
                else:
                    current_min = min(current_min, current_coins)
            
            minimum_coins_list[amount] = current_min
            return current_min
        
        compute_minimum_coins(amount)
        return minimum_coins_list[amount]
                

        