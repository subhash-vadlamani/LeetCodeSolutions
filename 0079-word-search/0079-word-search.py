class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        word_length = len(word)

        def dfs(i, j, index, visited):
            if index == word_length:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or board[i][j] != word[index]:
                return False
            
            visited.add((i, j))

            ans = (
                dfs(i, j + 1, index + 1, visited) or # move right
                dfs(i + 1, j, index + 1, visited) or # move down
                dfs(i, j - 1, index + 1, visited) or # move left
                dfs(i - 1, j, index + 1, visited) # move up
            )

            visited.remove((i, j))
            return ans
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, set()):
                    return True
        return False
        