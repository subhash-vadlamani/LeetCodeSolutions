class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        """
            I think I can sort the array first
            eg:
            [2, 3, 4, 6, 8, 16]
            find the longest subsequence of square streak
        """

        """
            Hint1 : With the given constraints, the maximum length
            that is possible is 5
        """
        seen = {}
        nums.sort(reverse=True)

        for i, x in enumerate(nums):
            if x * x in seen:
                seen[x] = seen[x * x] + 1
            else:
                seen[x] = 1
        
        ans = max(seen.values())
        if ans >= 2:
            return ans
        return -1
        