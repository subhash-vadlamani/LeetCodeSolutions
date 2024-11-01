class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        moves_dict = dict()


        def areGridIndicesInbound(i, j):
            """
                m -> Number of rows in the grid
                n -> Number of columns in the grid
                i -> row index of the element in the grid
                j -> column index of the element in the grid

                The method returns is the given index is inbounds or out of bounds
            """

            if (0 <= i < m) and (0 <= j < n):
                return True
            else:
                return False
        
        def dfs(i, j, number_of_moves):
            """
                i, j -> indices used to indicate the location of the element in the grid
                number_of_moves: variable that holds the number of moves taken to reach to that cell
            """

            """
                From (i, j) there are three possible moves:
                1. (i-1, j+1)
                2. (i, j+1)
                3. (i+1, j+1)
            """

            if not areGridIndicesInbound(i, j):
                return number_of_moves

            possible_moves = [
                (i - 1, j+1),
                (i, j+1),
                (i+1, j+1)
            ]

            result = number_of_moves
            current_value = grid[i][j]

            for new_i, new_j in possible_moves:
                if areGridIndicesInbound(new_i, new_j) and grid[new_i][new_j] > current_value:
                    new_move_dict_index = str(new_i) + str(new_j) + str(number_of_moves + 1)
                    if new_move_dict_index in moves_dict:
                        new_move_result = moves_dict[new_move_dict_index]
                    else:
                        new_move_result = dfs(new_i, new_j, number_of_moves + 1)
                        moves_dict[new_move_dict_index]  = new_move_result
                    result = max(result, new_move_result)
            
            return result

        current_max = float('-inf')

        for i in range(m):
            current_max = max(current_max, dfs(i, 0, 0))
        return current_max

        