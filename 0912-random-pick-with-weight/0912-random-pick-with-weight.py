import random
class Solution:

    def __init__(self, w: List[int]):
        total_weight = sum(w)
        self.outcomes = list(range(len(w)))
        self.my_weight_list = []
        for i in range(len(w)):
            self.my_weight_list.append(w[i]/total_weight)

        
        

    def pickIndex(self) -> int:
        return random.choices(self.outcomes, self.my_weight_list, k = 1)[0]

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()