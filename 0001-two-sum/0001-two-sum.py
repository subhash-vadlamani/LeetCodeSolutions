class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            O(n ** 2) -> pretty easy, double loop

            O(n) -> use dict to look up previously seen elements
        """
        previous_number_dict = dict()

        for i in range(len(nums)):
            required_number = target - nums[i]
            if required_number in previous_number_dict:
                return [previous_number_dict[required_number], i]
            previous_number_dict[nums[i]] = i
        
        