# class Solution:
#     def maxMatrixSum(self, matrix: List[List[int]]) -> int:

#         n = len(matrix)

#         """
#             dict to store the min magnitude negative number in a particular row.
#             If there does not exist an entry for a particular row in the dict,
#             that means that the row can be convereted to a row with all non-negative
#             numbers or the row does not have any non-negative numbers in the first place.
#         """
#         row_min_magnitude_negative_number = {}

#         for i in range(n):
#             current_row = matrix[0]

#             negative_number_count = 0

#             min_magnitude_negative_number = float('inf')

#             for element in current_row:
#                 if element < 0:
#                     negative_number_count += 1
#                     min_magnitude_negative_number = 


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        # Adjust if the count of negative numbers is odd
        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val

        return total_sum




        