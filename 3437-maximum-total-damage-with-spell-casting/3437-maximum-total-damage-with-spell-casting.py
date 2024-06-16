from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        damage_count = defaultdict(int)
        for p in power:
            damage_count[p] += 1
        
        # Step 2: Get the sorted list of unique spell damages
        unique_powers = sorted(damage_count.keys())
        
        # Step 3: Dynamic programming table
        dp = {}
        
        for i in range(len(unique_powers)):
            current_damage = unique_powers[i]
            current_total_damage = current_damage * damage_count[current_damage]
            
            if i == 0:
                dp[current_damage] = current_total_damage
            else:
                prev_damage = unique_powers[i-1]

                if current_damage - prev_damage == 1:
                    if current_damage - unique_powers[i - 2] == 2:
                        dp[current_damage] = max(dp[prev_damage], current_total_damage + dp.get(unique_powers[i-3], 0))
                    else:
                        dp[current_damage] = max(dp[prev_damage], current_total_damage + dp.get(unique_powers[i-2], 0))
                elif current_damage - prev_damage == 2:
                    dp[current_damage] = max(dp[prev_damage], current_total_damage + dp.get(unique_powers[i-2], 0))
                else:
                    dp[current_damage] = current_total_damage + dp[prev_damage]
        
        # The answer will be the maximum value in dp
        return max(dp.values())
            