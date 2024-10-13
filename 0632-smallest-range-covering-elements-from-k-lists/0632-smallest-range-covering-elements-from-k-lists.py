class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        min_heap = []
        max_value = float('-inf')
        
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        
        
        min_range = float('-inf'), float('inf')
        
        
        while min_heap:
            min_value, list_idx, element_idx = heapq.heappop(min_heap)
            
           
            if max_value - min_value < min_range[1] - min_range[0]:
                min_range = (min_value, max_value)
            

            if element_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
                max_value = max(max_value, next_value)
            else:
                break
        
        return list(min_range)
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


        