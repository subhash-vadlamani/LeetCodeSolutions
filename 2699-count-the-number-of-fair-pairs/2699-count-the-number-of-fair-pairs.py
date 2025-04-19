import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        """
            return the number of fair pairs
        """

        """
            step1: sort the numbers
        """

        nums_sorted = sorted(nums)

        """
            for every number in the nums, find the smallest and largest number that can be used
            to form a fair pair
        """

        answer = 0
        n = len(nums_sorted)
        for i in range(n):
            current_num = nums_sorted[i]

            current_lower = lower - current_num
            current_upper = upper - current_num

            left = bisect.bisect_left(nums_sorted, current_lower, i + 1, n)
            right = bisect.bisect_right(nums_sorted, current_upper, i + 1, n)
            
            answer += (right - left)
        return answer




        