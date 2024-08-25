class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        """
            Problem involves simulation.
            1st row, last column, last row, first column
            repeat again
        """

        L, R, T, B = 0, n - 1, 0, m - 1
        answer_list = []

        while L<= R and T <= B:

            for j in range(L, R + 1):
                answer_list.append(matrix[T][j])
            T += 1

            for i in range(T, B + 1):
                answer_list.append(matrix[i][R])
            R -= 1

            if T <= B:

                for j in range(R, L - 1, -1):
                    answer_list.append(matrix[B][j])
                B -= 1
            

            if L <= R:
                for i in range(B, T - 1, -1):
                    answer_list.append(matrix[i][L])
                L += 1

        
        return answer_list



        



        
        