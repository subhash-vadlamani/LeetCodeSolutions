class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_bracket = 0
        closed_bracket = 0

        for c in s:
            if c == "(":
                open_bracket += 1
            elif c == ")":
                if open_bracket > 0:
                    open_bracket -= 1
                else:
                    closed_bracket += 1
        answer = open_bracket + closed_bracket

        return answer
        