class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        height = [0] * (m + 1)
        max_area = 0

        for i in range(n):
            for j in range(m):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0

            stack = [-1]
            for j in range(m + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)

        return max_area
        