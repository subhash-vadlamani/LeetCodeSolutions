class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def get_count(n):
            count = 0
            while n:
                n = n & (n - 1)
                count += 1
            return count
        
        ans = []
        for i in range(n + 1):
            ans.append(get_count(i))
        return ans