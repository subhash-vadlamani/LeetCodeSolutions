class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_koko_finish(piles, h, k):
            # Local copy of piles to avoid mutating original array
            temp_piles = piles[:]
            hours_spent = 0
            for bananas in temp_piles:
                hours_spent += (bananas + k - 1) // k  # Equivalent to math.ceil(bananas / k)
                if hours_spent > h:  # If more hours are needed than available
                    return False
            return True

        # def can_koko_finish(piles, h, k):
        #     # k -> koko's banana eating speed
        #     piles_length = len(piles)
        #     i = 0
        #     for j in range(h):
        #         if i == piles_length:
        #             return True
        #         remaining_banans_in_pile = piles[i]
        #         remaining_banans_in_pile -= k
        #         if remaining_banans_in_pile <= 0:
        #             i += 1
        #         else:
        #             piles[i] = remaining_banans_in_pile
        #     if i != piles_length:
        #         return False

        min_pile_size = float('inf')
        max_pile_size = float('-inf')

        for i in range(len(piles)):
            if piles[i] < min_pile_size:
                min_pile_size = piles[i]
            
            if piles[i] > max_pile_size:
                max_pile_size = piles[i]
        
        i = 1
        j = max_pile_size

        minimum_koko_eating_speed = max_pile_size

        while i <= j:
            current_koko_eating_speed = (i + j) // 2

            if can_koko_finish(piles, h, current_koko_eating_speed):
                minimum_koko_eating_speed = current_koko_eating_speed
                j = current_koko_eating_speed - 1
            else:
                i = current_koko_eating_speed + 1
        
        return minimum_koko_eating_speed