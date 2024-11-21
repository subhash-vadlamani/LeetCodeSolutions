class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
            Initialize a matrix with all 0's initially to indicate that 
            all the nodes are initially free.

            1 -> Indicates a guard
            2 -> Indicates a Wall
            3 -> Indicates unsafe cells(cells that can be seen by guards)
        """

        matrix = [[0] * n for _ in range(m)] # Initialize the matrix

        for i, j in guards:
            matrix[i][j] = 1

        for i, j in walls:
            matrix[i][j] = 2
        
        def mark_direction(row, col, dr, dc):
            while 0 <= row < m and 0 <= col < n:
                if matrix[row][col] == 1 or matrix[row][col] == 2:
                    break
                if matrix[row][col] == 0:
                    matrix[row][col] = 3
                
                row += dr
                col += dc
        
        for i, j in guards:
            # Up
            mark_direction(i - 1, j, -1, 0)

            # Down
            mark_direction(i + 1, j, 1, 0)

            # Left
            mark_direction(i, j - 1, 0, -1)

            # Right
            mark_direction(i, j + 1, 0, 1)


        
        """
            All the guards and the unsafe cells have been populated. Now,
            we just return the count
        """
        final_count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    final_count += 1


        return final_count
        
        