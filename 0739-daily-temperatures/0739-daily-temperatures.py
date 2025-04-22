class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures_len = len(temperatures)
        stack = [] #(temepretures[i], i)
        answer = [0] * temperatures_len

        for i in range(temperatures_len - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                answer[i] = stack[-1][1] - i
            
            stack.append((temperatures[i], i))
        return answer

        