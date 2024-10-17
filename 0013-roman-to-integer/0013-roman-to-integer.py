class Solution:
    def romanToInt(self, s: str) -> int:
        value_dict = {}
        value_dict['I'] = 1
        value_dict['V'] = 5
        value_dict['X'] = 10
        value_dict['L'] = 50
        value_dict['C'] = 100
        value_dict['D'] = 500
        value_dict['M'] = 1000

        answer = 0
        character_list = []
        previous = 0

        for i in range(1, len(s)):
            previous_value = value_dict[s[previous]]
            current_value = value_dict[s[i]]

            if previous_value < current_value:
                character_list.append(-1)
            else:
                character_list.append(1)
            previous = i

        for i in range(0, len(character_list)):
            if character_list[i] == 1:
                answer += value_dict[s[i]]
            else:
                answer -= value_dict[s[i]]
                
        answer += value_dict[s[len(s)-1]]
        return answer

