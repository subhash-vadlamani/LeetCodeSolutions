class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            We are going to use a sliding window technique
            we are going to use two hashmaps
            one hashmap to store the charcter frequencies of the string p
            one hashmap to store the character frequencies of the substring of p
        """

        dict_p = dict()
        for char in p:
            if char not in dict_p:
                dict_p[char] = 1
            else:
                dict_p[char] += 1
        

        len_s = len(s)
        len_p = len(p)
        answer_list = []
        dict_substring = dict()

        if len_p > len_s:
            return answer_list

        l = 0
        r = len_p


        for i in range(r):
            if s[i] not in dict_substring:
                dict_substring[s[i]] = 1
            else:
                dict_substring[s[i]] += 1
        if dict_substring == dict_p:
            answer_list.append(l)
        while r < len_s:
            if s[r] not in dict_substring:
                dict_substring[s[r]] = 1
            else:
                dict_substring[s[r]] += 1
            
            if dict_substring[s[l]] == 1:
                dict_substring.pop(s[l])
            else:
                dict_substring[s[l]] -= 1
            
            r += 1
            l += 1

            if dict_substring == dict_p:
                answer_list.append(l)
        return answer_list

            
            
            


        