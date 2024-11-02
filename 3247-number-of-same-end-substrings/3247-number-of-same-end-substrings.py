class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:

        N = len(s)

        p = collections.defaultdict(list)
        for index, c in enumerate(s):
            p[c].append(index)
        ans = []
        for l, r in queries:
            total = 0
            for c in string.ascii_lowercase:
                lindex = bisect.bisect_left(p[c], l)
                rindex = bisect.bisect_right(p[c], r)
                nums = rindex - lindex

                total += comb(nums, 2) + nums
            ans.append(total)
        return ans



        # def compute_substring_list(s, queries):
        #     substring_list = []

        #     for l, r in queries:
        #         substring_list.append(s[l:r+1])
        #     return substring_list
        
        # def compute_number_of_same_end_substrings(s):
        #     """
        #         Method that returns the number of same end substrings in the given string
        #     """

        #     """
        #         Thought of a brute force approach with the O(N ** 2) but this will lead to TLE error.
        #     """

        #     """
        #         compute the prefix sum array of the substrings
        #         prefix_sum[i] : Represents the substring from [0:i], both included.
        #     """
        #     freq = {}
        #     result = 0

        #     for i in range(len(s)):
        #         char = s[i]

        #         result += 1
        #         if char in freq:
        #             result += freq[char]
                
        #         freq[char] = freq.get(char, 0) + 1
                
        #     return result

        # substring_list = compute_substring_list(s, queries)
        # # print(substring_list)
        # answer_dict = {}
        # answer_list = []
        # for substring in substring_list:
        #     if substring in answer_dict:
        #         current_substring_answer = answer_dict[substring]
        #     else:
        #         current_substring_answer = compute_number_of_same_end_substrings(substring)
        #         answer_dict[substring] = current_substring_answer
        #     answer_list.append(current_substring_answer)
        # return answer_list
            






        