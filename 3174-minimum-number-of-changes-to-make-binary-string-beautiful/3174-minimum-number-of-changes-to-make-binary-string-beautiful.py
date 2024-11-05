class Solution:
    def minChanges(self, s: str) -> int:

        """
            Approach:
            divide the string into substrings of each length 2
            count the changes to be made.
        """

        def flip_required(s):
            count_dict = {}

            for c in s:
                if c not in count_dict:
                    count_dict[c] = 1
                else:
                    count_dict[c] += 1
                
            if len(count_dict.keys()) == 1:
                return False
            else:
                return True
        
        """
            Construct the list of substrings
        """

        substring_list = []
        for i in range(0, len(s) - 1, 2):
            substring_list.append(s[i:i+2])
        
        print(substring_list)
        minimum_changes = 0
        for s in substring_list:
            if flip_required(s):
                minimum_changes += 1
        return minimum_changes

        