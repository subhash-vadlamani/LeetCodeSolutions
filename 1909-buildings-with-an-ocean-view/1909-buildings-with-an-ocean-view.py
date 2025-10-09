class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Monotonically decreasing Stack

        stack = [] #(index, height)

        for i in range(len(heights)):
            current_height = heights[i]

            if not stack or stack[-1][1] > current_height:
                stack.append((i, current_height))
            else:
                while stack and stack[-1][1] <= current_height:
                    stack.pop()
                stack.append((i, current_height))
        
        reverse_answer = []
        print(stack)
        while stack:
            current_item = stack.pop()
            reverse_answer.append(current_item[0])

        return reverse_answer[::-1]