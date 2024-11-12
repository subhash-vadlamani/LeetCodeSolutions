class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_len = len(fruits)

        if fruits_len <= 2:
            return fruits_len
        
        fruit_dict = dict()

        l = 0
        r = 2
        for i in range(r):
            if fruits[i] not in fruit_dict:
                fruit_dict[fruits[i]] = 1
            else:
                fruit_dict[fruits[i]] += 1
        curr_len, max_len = 2 , 2

        while r < fruits_len:
            current_fruit = fruits[r]
            if current_fruit in fruit_dict:
                fruit_dict[current_fruit] += 1
                curr_len = r - l + 1
                max_len = max(max_len, curr_len)
                r += 1
            else:
                fruit_dict_keys = fruit_dict.keys()

                if len(fruit_dict_keys) == 2:
                    """
                        Time to remove fruits[l]
                    """
                    if fruit_dict[fruits[l]] == 1:
                        fruit_dict.pop(fruits[l])
                    else:
                        fruit_dict[fruits[l]] -= 1
                    
                    l += 1
                else:
                    fruit_dict[current_fruit] = 1
                    curr_len = r - l + 1
                    max_len = max(max_len, curr_len)
                    r += 1

        return max_len
        