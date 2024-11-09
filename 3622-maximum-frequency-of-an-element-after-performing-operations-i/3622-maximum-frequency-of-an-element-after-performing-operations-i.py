class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        N = len(nums)
        f = collections.Counter(nums)

        def go(x):
            lindex = bisect.bisect_left(nums, x - k)
            rindex = bisect.bisect_right(nums, x + k)

            same = f[x]
            changes = min((rindex - lindex) - same, numOperations)
            return same + changes
        
        nums.sort()
        best = 0
        for i in range(nums[0], nums[-1] + 1):
            best = max(best, go(i))
        return best
        