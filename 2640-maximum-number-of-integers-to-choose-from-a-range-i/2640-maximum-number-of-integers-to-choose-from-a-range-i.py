class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        integer_count = 0
        banned = list(set(banned))
        banned.sort()

        for i in range(1, n+1):
            if i > maxSum:
                break
            if banned and i == banned[0]:
                banned.pop(0)
            else:
                integer_count += 1
                maxSum -= i
        return integer_count
        