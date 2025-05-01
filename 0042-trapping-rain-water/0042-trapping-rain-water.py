class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                sum_added = (min(leftMax, rightMax) - height[l])
                if sum_added > 0:
                    res += sum_added
                # res += max(leftMax - height[l], 0)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                sum_added = (min(leftMax, rightMax) - height[r])
                if sum_added > 0:
                    res += sum_added
                # res += max(rightMax - height[r], 0)
        return res
