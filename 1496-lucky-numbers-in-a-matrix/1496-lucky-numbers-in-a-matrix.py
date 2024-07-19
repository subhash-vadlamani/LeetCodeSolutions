class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        NUM1 = float('inf')
        NUM2 = float('-inf')
        minimum_list = [NUM1] * m
        maximum_list = [NUM2] * n

        for i in range(0, m):
            for j in range(0, n):
                current_number = matrix[i][j]

                if current_number < minimum_list[i]:
                    minimum_list[i] = current_number
                if current_number > maximum_list[j]:
                    maximum_list[j] = current_number
        
        final_answer_list = []

        for i in range(0, m):
            current_row_number = minimum_list[i]
            for j in range(0, n):
                current_column_number = maximum_list[j]

                if current_row_number == current_column_number:
                    final_answer_list.append(current_row_number)
        return final_answer_list


        