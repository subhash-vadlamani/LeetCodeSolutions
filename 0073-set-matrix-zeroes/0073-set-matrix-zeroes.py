class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        column_set = set()

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)
        
        for i in row_set:
            for j in range(0, len(matrix[i])):
                matrix[i][j] = 0
        
        for i in column_set:
            for j in range(0, len(matrix)):
                matrix[j][i] = 0
                
        