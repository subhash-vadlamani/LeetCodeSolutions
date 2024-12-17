class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        
        for i in range(0, len(nums)):
            if nums[i] in count_dict:
                return True
            count_dict[nums[i]] = 1
        return False
        