class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = []
        current_sum = 0

        for num in nums:
            current_sum += num
            prefix.append(current_sum)
        
        target = prefix[-1]
        answer = 0

        for i in range(0, len(nums) - 1):
            if prefix[i] >= target / 2 :
                answer += 1
        return answer
        

        