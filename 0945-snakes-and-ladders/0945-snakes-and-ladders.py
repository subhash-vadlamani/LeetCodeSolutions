from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def access_boustrophedon_element(matrix, index):
            n = len(matrix[0])  # number of columns
            total_elements = n * n
            row = (total_elements - 1 - (index - 1)) // n
            col = (index - 1) % n
            if (n - row) % 2 == 0:  # even row (from bottom), reverse column
                col = n - 1 - col
            return matrix[row][col]

        start_element = (1, 0)
        queue = deque([start_element])
        visited = set()
        
        while queue:
            current, moves = queue.popleft()
            
            if current in visited:
                continue
            
            if current == n * n:
                return moves
            
            visited.add(current)
            
            for i in range(1, 7):
                next_square = current + i
                if next_square <= n * n:
                    next_index_value = access_boustrophedon_element(board, next_square)
                    if next_index_value != -1:
                        next_square = next_index_value
                    if next_square not in visited:
                        queue.append((next_square, moves + 1))
        
        return -1

# # Example usage:
# board = [
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 35, -1, -1, 13, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 15, -1, -1, -1, -1]
# ]
# solution = Solution()
# result = solution.snakesAndLadders(board)
# print(result)  # Output: least number of moves to reach the end or -1 if not possible