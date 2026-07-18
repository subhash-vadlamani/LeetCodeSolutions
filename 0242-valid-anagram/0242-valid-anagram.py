class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def generate_char_dict(my_string:str) -> dict:
            my_string_dict = {}
            for my_char in my_string:
                if my_char not in my_string_dict:
                    my_string_dict[my_char] = 1
                else:
                    my_string_dict[my_char] += 1
            return my_string_dict
        
        my_s_dict = generate_char_dict(s)
        my_t_dict = generate_char_dict(t)

        # print(f"my_s_dict is ${my_s_dict}")
        # print(f"my_t_dict is ${my_t_dict}")

        return (my_s_dict == my_t_dict)
        