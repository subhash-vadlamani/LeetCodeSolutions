class Solution:
    def minimumPushes(self, word: str) -> int:
        char_dict = dict()

        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        sorted_keys = sorted(char_dict, key = lambda k: char_dict[k], reverse=True)

        one_count = [8, 0]
        two_count = [8,0]
        three_count = [8,0]
        four_count = [2,0]

        for key in sorted_keys:
            if one_count[0]:
                one_count[0] -= 1
                one_count[1] += char_dict[key]
            elif two_count[0]:
                two_count[0] -= 1
                two_count[1] += char_dict[key]
            elif three_count[0]:
                three_count[0] -= 1
                three_count[1] += char_dict[key]
            else:
                four_count[0] -= 1
                four_count[1] += char_dict[key]
        
        minimum_pushes = 0

        minimum_pushes = (one_count[1]) + (2 * two_count[1]) + (3 * three_count[1]) + (4 * four_count[1])

        return minimum_pushes
        