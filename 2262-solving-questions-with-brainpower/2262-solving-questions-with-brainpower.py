class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        question_count = len(questions)
        dp = [-1] * question_count

        def calculate_most_points(questions, i):

            # Base case
            if i >= question_count:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            """
                2 choices,
                Either I pick the question to solve it, or I don't pick it
            """
            most_points = max(questions[i][0] + calculate_most_points(questions, i + questions[i][1] + 1), calculate_most_points(questions, i + 1))

            dp[i] = most_points

            return dp[i]
        
        return calculate_most_points(questions, 0)
        