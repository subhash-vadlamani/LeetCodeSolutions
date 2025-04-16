class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime_digit_set = {2, 3, 5, 7}
        MOD = 10 ** 9 + 7

        """
            complement counting method?
            a digit string is good  if digits

            eg1:
            n = 1, ans = 5

            n = 4, ans = 5 * 4 * 5 * 4
        """

        if n == 1:
            return 5
        
        if n % 2 == 0:
            result_1 = pow(4, n//2, MOD)
            result_2 = pow(5, n//2, MOD)

            answer = (result_1 * result_2) % MOD
        else:
            result_1 = pow(4, (n - 1) // 2, MOD)
            result_2 = pow(5, (n - 1) // 2, MOD)
            
            answer = (result_1 * result_2 * 5) % MOD
        
        return answer

            




        