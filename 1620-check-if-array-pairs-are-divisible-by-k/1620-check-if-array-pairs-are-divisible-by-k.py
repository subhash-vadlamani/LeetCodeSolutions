class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulo_dict = dict()

        for i in range(0, len(arr)):
            current_modulo = arr[i] % k
            if current_modulo not in modulo_dict:
                modulo_dict[current_modulo] = 1
            else:
                modulo_dict[current_modulo] += 1
        
        i = 1
        j = k - 1

        if modulo_dict.get(0, 0) % 2 != 0:
            return False
        if k % 2 == 0:
            if modulo_dict.get(k/2 , 0) % 2 != 0:
                return False

        while i < j:
            if modulo_dict.get(i, 0) != modulo_dict.get(j, 0):
                return False
            i += 1
            j -= 1
        return True
        
        