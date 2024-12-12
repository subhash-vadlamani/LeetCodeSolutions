class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        def sort(nums):
            N = len(nums)
            i = 0

            while(i < N):
                correct_index = nums[i] - 1

                if nums[correct_index] != correct_index + 1:
                    swap(nums, i, correct_index)
                else:
                    i += 1
            return nums
        

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        nums = sort(nums)
        N = len(nums)
        ans = []

        for i in range(N):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans
        