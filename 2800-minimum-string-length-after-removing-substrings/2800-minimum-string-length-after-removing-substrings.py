class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" in s:
                s = s.replace("AB", "")
                continue
            if "CD" in s:
                s = s.replace("CD", "")
                continue
            break
        return len(s)
        