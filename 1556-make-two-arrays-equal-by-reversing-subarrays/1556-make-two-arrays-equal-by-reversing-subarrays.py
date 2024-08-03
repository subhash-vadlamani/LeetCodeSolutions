class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_dict = dict()

        for element in target:
            if element not in target_dict:
                target_dict[element] = 1
            else:
                target_dict[element] += 1

        arr_dict = dict()


        
        for element in arr:
            if element not in arr_dict:
                arr_dict[element] = 1
            else:
                arr_dict[element] += 1
        
        for key in target_dict.keys():
            target_dict_value = target_dict[key]

            if key not in arr_dict or arr_dict[key] != target_dict_value:
                return False
        return True

        