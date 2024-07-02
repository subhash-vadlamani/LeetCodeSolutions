class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for i in range(0, len(arr)):
            if count == 3:
                return True
            if arr[i] % 2 == 1:
                count += 1
            else:
                count = 0
        if count == 3:
            return True
        return False
        