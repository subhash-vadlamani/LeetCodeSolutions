from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        # answer[i] will store the number of people person i can see.
        answer = [0] * n
        # The stack will store heights of people to the right,
        # maintained in a monotonically decreasing order.
        stack = []

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            current_height = heights[i]
            visible_count = 0
            
            # While stack has people and the current person is taller than 
            # the person at the top of the stack (closest to the right).
            while stack and current_height > stack[-1]:
                # This person is visible. Pop them as they are now blocked
                # from view for anyone to the left of the current person.
                stack.pop()
                visible_count += 1
            
            # If the stack is not empty after the loop, it means there is a
            # taller person to the right that blocks further view.
            # The current person can see this one taller person.
            if stack:
                visible_count += 1
            
            answer[i] = visible_count
            
            # Push the current person's height onto the stack for future
            # calculations for people to the left.
            stack.append(current_height)
            
        return answer
