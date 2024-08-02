class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        """
            This variable 'total' holds the total number of 1's in the list
        """
        total = 0
        nums_length = len(nums)

        for i in range(0, len(nums)):
            if nums[i] == 1:
                total += 1
        
        if total == nums_length - 1 or total == 0:
            return 0
        
        i = 0
        j = total - 1

        min_swaps = 10 ** 20
        swaps = 0

        for k in range(i, j+1):
            if nums[k] == 0:
                swaps += 1
        if swaps < min_swaps:
            min_swaps = swaps

        while True:
            i_value = nums[i]

            if i_value == 0:
                swaps -= 1

            i = (i + 1) % nums_length
            j = (j + 1) % nums_length

            j_value = nums[j]
            
            if j_value == 0:
                swaps += 1
            
            if swaps < min_swaps:
                min_swaps = swaps
            
            if i == 0 and j == total - 1:
                break
        return min_swaps
                
            
