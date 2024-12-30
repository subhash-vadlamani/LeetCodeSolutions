from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_dict = defaultdict(list)
        digit_dict[2] = ["a", "b", "c"]
        digit_dict[3] = ["d", "e", "f"]
        digit_dict[4] = ["g", "h", "i"]
        digit_dict[5] = ["j", "k", "l"]
        digit_dict[6] = ["m", "n", "o"]
        digit_dict[7] = ["p", "q", "r", "s"]
        digit_dict[8] = ["t", "u", "v"]
        digit_dict[9] = ["w", "x", "y" , "z"]

        total_length = len(digits)
        
        def dfs(i, cur):
            if i == total_length:
                if cur:
                    res.append("".join(cur))
                return
            
            for letter in digit_dict[int(digits[i])]:
                cur.append(letter)
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return res



        
        