class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Build a prefix array from the string

        boxes_list = [int(val) for val in list(boxes)]
        
        current = 0
        boxes_prefix_list = [0]
        for i in range(len(boxes_list)):
            current += boxes_list[i]
            boxes_prefix_list.append(current)
            
        
        def calculate_cost(prefix_list, i):
            # calculate the cost to move all the balls to index i
            cost = 0
            for j in range(1, len(prefix_list)):
                # Number of balls in index j
                current_index_ball_count = prefix_list[j] - prefix_list[j - 1]
                cost += (current_index_ball_count * (abs(j - i)))
            return cost
        
        answer = []
        for k in range(1, len(boxes_prefix_list)):
            answer.append(calculate_cost(boxes_prefix_list, k))
        return answer


        







        