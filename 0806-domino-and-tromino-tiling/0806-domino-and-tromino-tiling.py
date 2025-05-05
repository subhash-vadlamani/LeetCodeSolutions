class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        # this is the number of ways to get an 2 x N with one extra bit hanging out
        def get_odd(N):
            if N <= 0:
                return 0
            
            # one vertical ->
            one_vertical = get_odd(N - 1)

            # tromino ->
            tromino  = get_even(N - 1)
            
            return (one_vertical + tromino) % MOD
            

        

        @cache
        # this is the number of ways to get an 2 x N with nothing left over
        def get_even(N):

            if N == 0:
                return 1
            elif N < 0:
                return 0
            
            one_vertical = get_even(N - 1)
            two_horizontal = get_even(N - 2)

            # tromino

            tromino = 2 * get_odd(N - 2)

            return (one_vertical + two_horizontal + tromino) % MOD
        
        return get_even(n)


        