class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        max_element = max(nums)

        left = 0
        right = 0
        max_element_count = 0
        answer = 0

        while right < len(nums):

            if nums[right] == max_element:
                max_element_count += 1
            
            while max_element_count >= k:
                if nums[left] == max_element:
                    max_element_count -= 1
                left += 1
            
            answer += left
            right += 1
        
        return answer


            


        