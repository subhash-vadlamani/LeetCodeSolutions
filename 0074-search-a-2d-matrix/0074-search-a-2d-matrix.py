import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            I want to do binary search on the first column to know
            which row to search
        """

        def get_row(matrix, target):
            low = 0
            high = len(matrix) - 1

            while low <= high:
                mid = low + ((high - low) // 2)

                if matrix[mid][0] == target:
                    return mid
                elif target < matrix[mid][0]:
                    high = mid - 1
                else:
                    low = mid + 1
            return low - 1
        
        required_row = get_row(matrix, target)
        if required_row < 0:
            return False
        
        def search_row(matrix, row_number, target):
            low = 0
            high = len(matrix[0]) - 1

            while low <= high:
                mid = low + ((high - low) // 2)

                if matrix[row_number][mid] == target:
                    return True
                elif target < matrix[row_number][mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        
        return search_row(matrix, required_row, target)



        