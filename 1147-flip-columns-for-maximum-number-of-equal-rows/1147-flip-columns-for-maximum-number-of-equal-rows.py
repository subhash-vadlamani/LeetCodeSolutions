class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        my_map = dict()

        def flip_string(s):
            new_list = []
            for c in s:
                if c == '0':
                    new_list.append('1')
                else:
                    new_list.append('0')
            return "".join(new_list)
        
        for current_list in matrix:
            current_string = "".join(map(str, current_list))
            if current_string[0] == '0':
                if current_string in my_map:
                    my_map[current_string] += 1
                else:
                    my_map[current_string] = 1
            else:
                new_string = flip_string(current_string)

                if new_string in my_map:
                    my_map[new_string] += 1
                else:
                    my_map[new_string] = 1
        return max(my_map.values())
        