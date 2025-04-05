from collections import Counter
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
            maintain a list of indices that need to be removed
        """

        remove_char_index_list = []

        # stack to see which element to remove
        char_stack = [] # (char_value, index)

        for i in range(len(s)):
            current_char = s[i]

            """
                3 cases
                1. character is '('
                2. character is ')'
                3. character is alpha numeric

            """

            if current_char == '(':
                char_stack.append((current_char, i))
            elif current_char == ')':
                if not char_stack:
                    remove_char_index_list.append(i)
                else:
                    char_stack.pop()
        
        # add the remaining elements of the char_stack to the list of elements to be removed

        for element in char_stack:
            remove_char_index_list.append(element[1])

        
        
        # include_element_index_list = list(set(range(len(s))) - set(remove_char_index_list))

        remove_counter = Counter(remove_char_index_list)
        include_element_index_list = []

        for item in list(range(len(s))):
            if remove_counter[item]:
                remove_counter[item] -= 1
            else:
                include_element_index_list.append(item)
        

        answer_list = []
        for index in include_element_index_list:
            answer_list += list(s[index])
        
        return "".join(answer_list)
        




        