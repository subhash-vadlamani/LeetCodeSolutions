class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
            Write a method that takes the list of elements
            and outputs a dict of numbers and count of set bits for 
            those numbers
        """

        def countSetBits(binary_rep):
            set_bits_count = 0

            for c in binary_rep:
                if c == '1':
                    set_bits_count += 1
            return set_bits_count
        def createSetBitsDict(nums):
            set_bits_dict = dict()
            for num in nums:
                binary_rep = bin(num)[2:]
                if num not in set_bits_dict:
                    binary_rep = str(bin(num)[2:])
                    set_bits_dict[num] = countSetBits(binary_rep)
            return set_bits_dict
        
        set_bits_dict = createSetBitsDict(nums)

        """
            Splitting the array into segments where each segment has same number of 
            set bits
        """

        segment_list = []
        previous_set_bits = set_bits_dict[nums[0]]
        previous_list = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            current_set_bits = set_bits_dict[nums[i]]

            if current_set_bits == previous_set_bits:
                previous_list.append(nums[i])
            else:
                previous_set_bits = current_set_bits
                segment_list.append(previous_list)
                previous_list = [nums[i]]
        
        segment_list.append(previous_list)

        if len(segment_list) == 1:
            return True
        
        for i in range(1, len(segment_list)):
            prev_segment_elements = segment_list[i-1]
            current_segment_elements = segment_list[i]

            if not(max(prev_segment_elements) < min(current_segment_elements)):
                return False
        return True
            
        




        