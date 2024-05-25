class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Step 1: convert the unsurrounded regions into T

        def dfs(r, c):
            if (r < 0 or r > rows - 1) or (c < 0 or c > cols - 1) or (board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    dfs(r, c)
        


        # Step 2: the 'O's that still remin are surrounded. So 'O' -> 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
                
                
        

#         # Step 3: The 'T's should be converted back to 'O's

#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "T":
#                     board[r][c] = "O"


        

        
        