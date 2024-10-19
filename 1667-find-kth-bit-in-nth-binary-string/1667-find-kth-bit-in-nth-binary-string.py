class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def get_inverted_string(s):
            inverted_string = ""
            for char in s:
                if char == '0':
                    inverted_string += '1'
                else:
                    inverted_string += '0'
            return inverted_string
        
        dp = ["0"] * (n + 1)

        for i in range(2, n+1):
            
            dp[i] = dp[i - 1] + "1" + get_inverted_string(dp[i - 1])[::-1]
        
        required_string = dp[n]
        required_bit = required_string[k-1]
        return required_bit
        