class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        element_list = [item for sublist in grid for item in sublist]

        element_list.sort()

        # check if possible
        required_mod = element_list[0] % x

        for i in range(1, len(element_list)):
            if element_list[i] % x != required_mod:
                return -1

        def median(sorted_list):
            n = len(sorted_list)
            mid = n // 2
            return sorted_list[mid - 1] if n % 2 == 0 else sorted_list[mid]
        
        # find median
        current_median = median(element_list)

        # count the number of operations to make all the elements equal to the median
        min_operations = 0
        for element in element_list:
            min_operations += abs(element - current_median) // x
        
        return min_operations


        