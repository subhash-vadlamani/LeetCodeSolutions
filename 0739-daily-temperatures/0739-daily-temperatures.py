class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        list_length = len(temperatures)
        answer = [0] * list_length
        stack = []

        for i in range(list_length - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])
        return answer
            
        