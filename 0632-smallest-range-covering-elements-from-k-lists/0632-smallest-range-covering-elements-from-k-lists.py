import heapq 
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        max_val = float('-inf')
        range_start = 0
        range_end = float('inf')
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(pq, (nums[i][0], i, 0))  # (value, list index, element index)
            max_val = max(max_val, nums[i][0])  # Track the maximum value in the current range

        # Process the heap
        while len(pq) == len(nums):  # Continue while the heap contains elements from all lists
            min_val, row, col = heapq.heappop(pq)
            
            # Update the range if the current range is smaller
            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val

            # If there is a next element in the same list, push it to the heap
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(pq, (next_val, row, col + 1))
                max_val = max(max_val, next_val)  # Update the maximum value
            else:
                # If any list is exhausted, stop the process
                break

        return [range_start, range_end]




        
        # nums_length = len(nums)
        # sorted_list_pointers = [0] * nums_length

        # current_minimum_range_length = float('inf')
        # current_minimum_range_list = [float('-inf'), float('inf')]

        # while True:
        #     current_list_pointer_elements = []
        #     for i in range(0, nums_length):
        #         current_list = nums[i]
        #         current_list_pointer = sorted_list_pointers[i]
        #         current_list_element = current_list[current_list_pointer]
        #         current_list_pointer_elements.append(current_list_element)

        #     current_list_pointer_elements.sort()


        