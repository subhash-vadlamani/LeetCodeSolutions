class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_assigned = {}
        candies_assigned[0] = 1
        prev_index = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                current_index_candies = candies_assigned[i-1] + 1
            else:
                current_index_candies = 1
            candies_assigned[i] = current_index_candies
        for i in range(len(ratings) - 1, -1, -1):
            if i > 0 and i < len(ratings) - 1:
                if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                    current_index_candies = max(candies_assigned[i-1], candies_assigned[i+1]) + 1
                elif ratings[i] > ratings[i-1]:
                    current_index_candies = candies_assigned[i-1] + 1
                elif ratings[i] > ratings[i+1]:
                    current_index_candies = candies_assigned[i+1] + 1
                else:
                    current_index_candies = candies_assigned[i]
                
                candies_assigned[i] = current_index_candies
            else:
                if i == len(ratings) - 1 :
                    if ratings[i] > ratings[i - 1]:
                        current_index_candies = candies_assigned[i-1] + 1
                    else:
                        current_index_candies = candies_assigned[i]
                else:
                    if ratings[i] > ratings[i + 1]:
                        current_index_candies = candies_assigned[i+1] + 1
                    else:
                        current_index_candies = candies_assigned[i]
                candies_assigned[i] = current_index_candies
        
        total_candies = 0

        for key in candies_assigned:
            total_candies += candies_assigned[key]
        return total_candies
                

