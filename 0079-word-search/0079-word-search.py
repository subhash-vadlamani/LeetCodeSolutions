class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
            dfs problem
        """

        """
            i,j: represent the indices of the current character
            k: represents the index of the character within the word that we are searching for
        """
        m = len(board)
        n = len(board[0])
        def dfs(i, j, k):
            if not ((0 <= i < m) and (0 <= j < n)):
                return False
            
            board_character = board[i][j]
            required_word_character = word[k]

            if board_character != required_word_character:
                return False
            if k == len(word) - 1:
                return True
            
            # (i, j + 1), (i, j - 1), (i-1, j), (i+1, j)
            temp, board[i][j] = board[i][j], '#'

            # dfs(i, j+1, k+1)
            # dfs(i, j-1, k+1)
            # dfs(i-1, j, k+1)
            # dfs(i+1, j, k+1)

            result = dfs(i, j+1, k+1) or dfs(i, j-1, k+1) or dfs(i-1, j, k+1) or dfs(i+1, j, k+1)
            board[i][j] = temp
            return result
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
            

        