from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
            Breadth first search
        """

        q = deque()
        visit = set()
        total_candies = 0
        keys_found_so_far = set() # to open a box, either it has to be open or we should have it's key
        for box in initialBoxes:
            q.append(box)
        
        while q:
            additional_candies = 0 # candies that have been found in the current round
            for _ in range(len(q)):
                current_box = q.popleft()
                
                
                # check if box has not been visited so far
                if current_box not in visit:
                    # check if the box is open or we have found the key
                    # box can be opened
                    if (status[current_box] == 1 or current_box in keys_found_so_far):
                        additional_candies += candies[current_box]
                        for key in keys[current_box]:
                            keys_found_so_far.add(key)
                        
                        for box in containedBoxes[current_box]:
                            q.append(box)
                        
                        visit.add(current_box)
                    # box cannot be opened
                    else:
                        # add the box to the queue hoping that it can be opened later
                        q.append(current_box)
                
            if additional_candies:
                total_candies += additional_candies
            else:
                break
        
        return total_candies










        