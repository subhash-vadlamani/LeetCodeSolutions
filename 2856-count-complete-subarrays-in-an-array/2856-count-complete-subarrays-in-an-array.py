class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        array_set = set(nums)
        # print(array_set)
        answer = 0
        nums_len = len(nums)

        for i in range(nums_len):

            current_set = set()

            for j in range(i, nums_len):
                current_set.add(nums[j])
                # print(current_set)

                if current_set == array_set:
                    answer += 1
        
        return answer

        