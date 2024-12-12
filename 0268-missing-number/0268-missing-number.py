class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        def sort(nums):
            i = 0
            N = len(nums)
            while(i < N):
                correct_index = nums[i]
                if correct_index != i and correct_index != N:
                    swap(nums, correct_index, i)
                else:
                    i += 1
            return nums
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        nums = sort(nums)
        N = len(nums)

        for i in range(N):
            if i != nums[i]:
                return i
        
        return N
        