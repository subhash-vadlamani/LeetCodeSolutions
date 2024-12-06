class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # start_list = ['0']*26
        # start_string = "".join(start_list)
        str_dict = dict()

        for current_str in strs:
            current_key_list = [0] * 26
            for char in current_str:
                current_key_list[ord(char) - ord('a')] += 1
            
            current_key = "".join(str(current_key_list))

            if current_key not in str_dict:
                str_dict[current_key] = [current_str]
            else:
                str_dict[current_key].append(current_str)

        return list(str_dict.values())


        