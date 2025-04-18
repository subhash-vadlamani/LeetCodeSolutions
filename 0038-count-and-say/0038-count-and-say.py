class Solution:
    def countAndSay(self, n: int) -> str:

        def rle(my_str):
            rle_string = ""

            prev_char = None
            curr_count = 0
            for curr_char in my_str:

                if prev_char and prev_char != curr_char:
                    rle_string += str(curr_count)
                    rle_string += prev_char
                    curr_count = 1
                else:
                    curr_count += 1
                
                prev_char = curr_char
            
            rle_string += str(curr_count)
            rle_string += prev_char

            return rle_string

        
        def dfs(i):
            if i == "1":
                return "1"
            
            return rle(dfs(str(int(i) - 1)))
        
        answer = dfs(str(n))
        return answer
            


        