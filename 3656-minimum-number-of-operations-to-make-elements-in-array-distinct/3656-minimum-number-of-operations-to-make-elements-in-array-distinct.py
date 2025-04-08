class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        """
            create a list that keeps the track of element freq
        """

        freq_list = [0] * 101

        for num in nums:
            freq_list[num] += 1
        
        def remove_trailing_elements():
            for i in range(3):
                if nums:
                    popped_num = nums.pop(0)
                    freq_list[popped_num] -= 1
        
        operation_count = 0

        while max(freq_list) > 1:
            remove_trailing_elements()
            operation_count += 1
        
        return operation_count
