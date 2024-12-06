class Solution:
    def canChange(self, start: str, target: str) -> bool:
        string_length = len(start)
        start_order = ""
        target_order = ""
        start_dict = dict()
        target_dict = dict()
        
        for i in range(string_length):
            if start[i] != '_':
                start_order += start[i]
                if start[i] not in start_dict:
                    start_dict[start[i]] = [i]
                else:
                    start_dict[start[i]].append(i)
        
        for i in range(string_length):
            if target[i] != '_':
                target_order += target[i]
                if target[i] not in target_dict:
                    target_dict[target[i]] = [i]
                else:
                    target_dict[target[i]].append(i)
        
        if start_order != target_order:
            return False
        
        for key in start_dict.keys():
            if key == 'L':
                start_L_indices = start_dict[key]
                target_L_indices = target_dict[key]

                for i in range(len(start_L_indices)):
                    if start_L_indices[i] < target_L_indices[i]:
                        return False
            
            else:
                start_R_indices = start_dict[key]
                target_R_indices = target_dict[key]

                for i in range(len(start_R_indices)):
                    if start_R_indices[i] > target_R_indices[i]:
                        return False
        
        return True
