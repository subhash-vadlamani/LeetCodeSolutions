class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = dict()

        for s in strs:
            sorted_s = (sorted(s))
            sorted_string = ""
            for char in sorted_s:
                sorted_string += char
            # print(sorted_string)
            if sorted_string not in my_dict:
                my_dict[sorted_string] = [s]
            else:
                my_dict[sorted_string].append(s)
        
        # print(my_dict)
        answer = list(my_dict.values())
        return answer

        # def get_tuple_key(s):
        #     dict_key = dict()

        #     for char in s:
        #         if char not in dict_key:
        #             dict_key[char] = 1
        #         else:
        #             dict_key[char] += 1
        #     key_as_tuple = tuple(dict_key.items())
        #     return key_as_tuple
        
        # anagram_dict = dict()

        # for s in strs:
        #     current_string_tuple_key = get_tuple_key(s)

        #     if current_string_tuple_key not in anagram_dict:
        #         anagram_dict[current_string_tuple_key] = [s]
        #     else:
        #         anagram_dict[current_string_tuple_key].append(s)
        
        # answer = list(anagram_dict.values())
        # return answer




        
        