class Solution:
    def maxScore(self, s: str) -> int:
        total_zero_count = 0
        total_one_count = 0

        for c in s:
            if c == '0':
                total_zero_count += 1
            else:
                total_one_count += 1
        
        max_score = float('-inf')
        left_zero_count = 0
        left_one_count = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zero_count += 1
            else:
                left_one_count += 1
            
            max_score = max(max_score, (left_zero_count + (total_one_count - left_one_count)))
        return max_score
        