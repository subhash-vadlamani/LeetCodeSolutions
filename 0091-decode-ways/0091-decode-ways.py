class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0 or s[0] == '0':
            return 0  # No valid decoding if string is empty or starts with '0'
        
        dp = [0] * (N + 1)  # Create a DP array of size N + 1
        dp[0] = 1  # Base case: one way to decode an empty string
        dp[1] = 1  # Base case: one way to decode a string of length 1 if it's not '0'
        
        for i in range(2, N + 1):
            one_digit = int(s[i - 1])  # Single digit decoding
            two_digit = int(s[i - 2:i])  # Two-digit decoding
            
            # Check for valid one-digit decode
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            
            # Check for valid two-digit decode
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[N]