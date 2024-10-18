
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        current_min_sum_difference = float('inf')

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                current_sum_difference = abs(threeSum - target)
                if current_sum_difference < current_min_sum_difference:
                    res = threeSum
                    current_min_sum_difference = current_sum_difference
                if threeSum > target:
                    r -= 1
                    
                elif threeSum < target:
                    l += 1
                else:
                    # res.append([a, nums[l], nums[r]])
                    return res

                    # l += 1
                    # while nums[l] == nums[l - 1] and l < r:
                    #     l += 1
        return res
        