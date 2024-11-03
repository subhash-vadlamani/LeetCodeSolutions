class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = list(s)
        goal_list = list(goal)

        """
            list indexing
            my_list[i:j]
        """
        s_len = len(s_list)
        goal_len = len(goal_list)

        if s_len != goal_len:
            return False

        for i in range(s_len):
            current_string =''.join(s_list[i:s_len]) + ''.join(s_list[0:i])
            # print(current_string)
            if current_string == goal:
                return True
        return False

        