import string
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
            If, we were able to generate a defaultdict with key as the original character
            value as a set of equivalent characters(sorting is O(1) since it's just 26 characters),
            we can pick the characters from each set of the default dict.
        """
        equivalent_dict = defaultdict(set)

        """
            We can construct the default dict in 4 steps
            given equivalence, Reflexivity, Symmetry, Transitivity
        """

        for char in string.ascii_lowercase:
            equivalent_dict[char].add(char)
        s_len = len(s1)
        # given equivalence , reflexivity, symmetry
        for i in range(s_len):
            equivalent_dict[s1[i]].add(s2[i])
            equivalent_dict[s1[i]].add(s1[i])
            equivalent_dict[s2[i]].add(s1[i])
            equivalent_dict[s2[i]].add(s2[i])

        
        while True:
            
            new_elements_added = False
            for key, val in equivalent_dict.items():
                additional_element_set = set()
                for char in val:
                    additional_element_set |= equivalent_dict[char]
                
                new_set = equivalent_dict[key] | additional_element_set
                if new_set != equivalent_dict[key]:
                    new_elements_added = True
                    equivalent_dict[key] = new_set
                # equivalent_dict[key] |= additional_element_set
                
                # final_new_sorted_set = sorted(equivalent_dict[key] | additional_element_set)
                # equivalent_dict[key] = final_new_sorted_set
            
            if not new_elements_added:
                break
        
        final_char_list = []

        for i in range(len(baseStr)):
            final_char_list.append(min(equivalent_dict[baseStr[i]]))
        
        print(equivalent_dict)
        return "".join(final_char_list)
        



        
        



        