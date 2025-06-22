class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
            2 cases:
            1. we don't need to use fill(len(s) % k == 0)
            2. we need to use fill (len(s) % k != 0)
        """

        s_len = len(s)
        answer = []
        if s_len % k == 0:
            start = 0
            while True:
                answer.append(s[start:(start+k)])
                start = start + k
                if start == s_len:
                    break
        else:
            required_count = s_len // k
            current_count = 0
            start = 0

            while current_count < required_count:
                answer.append(s[start:(start + k)])
                start = start + k
                current_count += 1
            number_of_fill_characters = k - (s_len % k)
            final_string = s[start:s_len] + fill * number_of_fill_characters
            answer.append(final_string)
        
        return answer

        