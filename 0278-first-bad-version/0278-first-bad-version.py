# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid) and ((mid - 1) == 0 or not isBadVersion(mid - 1)):
                return mid
            
            elif isBadVersion(mid) and (isBadVersion(mid - 1)):
                right = mid
            else:
                left = mid + 1
        
        if isBadVersion(left):
            return left
        
        