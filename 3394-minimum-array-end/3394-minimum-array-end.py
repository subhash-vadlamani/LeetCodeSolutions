class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        bn = collections.deque(bin(n)[2:][::-1])
        bx = bin(x)[2:][::-1]

        ans = []

        for c in bx:
            if c == "1":
                ans.append("1")
            else:
                if len(bn) > 0:
                    ans.append(bn.popleft())
                else:
                    ans.append("0")
        while len(bn) > 0:
            ans.append(bn.popleft())

            
            
        return int("".join(ans[::-1]), 2)
        