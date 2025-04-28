from typing import List
import bisect

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Build prefix sum array
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        answer = 0

        # Step 2: For every ending index, binary search the earliest starting index
        for end in range(1, n + 1):  # prefix_sum[1] corresponds to nums[0]
            low = 0
            high = end - 1
            best = end

            while low <= high:
                mid = (low + high) // 2
                subarray_sum = prefix_sum[end] - prefix_sum[mid]
                length = end - mid
                score = subarray_sum * length

                if score < k:
                    best = mid
                    high = mid - 1  # try to find an even earlier start
                else:
                    low = mid + 1  # need smaller subarrays
            
            # all subarrays [best, end-1], [best+1, end-1], ..., [end-1, end-1] are valid
            answer += end - best

        return answer
