class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = dict()

        for ch in s:
            if ch not in my_dict:
                my_dict[ch] = 1
            else:
                my_dict[ch] += 1
        
        ordered_freq = sorted(my_dict.values())

        for i in range(len(ordered_freq) -1 , -1, -1):
            current_val =ordered_freq[i]
            if current_val % 2 != 0:
                max_odd_freq = current_val
                break
        
        for i in range(len(ordered_freq)):
            current_val = ordered_freq[i]

            if current_val % 2 == 0:
                min_even_freq = current_val
                break
        
        return max_odd_freq - min_even_freq
        