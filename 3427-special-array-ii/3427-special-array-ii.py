class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        N = len(nums)

        breaks = []

        for i in range(N - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                breaks.append(i)
        
        ans = []
        for s, e in queries:
            left = bisect.bisect_left(breaks, s)
            right = bisect.bisect_left(breaks, e)

            ans.append(left == right)
        return ans
        