from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        height_matrix = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque() # (i, j) tuple is added

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height_matrix[i][j] = 0
                    q.append((i, j))
                    # visit.add((i, j))
        
        # visit = set() # (i, j) tuple is added
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                current_i, current_j = q.popleft()
                # if (current_i, current_j) in visit:
                #     continue
                # visit.add((current_i, current_j))
                current_height = height_matrix[current_i][current_j]
                for di, dj in directions:
                    new_i, new_j = current_i + di, current_j + dj
                    if new_i in range(m) and new_j in range(n) and height_matrix[new_i][new_j] == -1:
                        height_matrix[new_i][new_j] = 1 + current_height
                        q.append((new_i, new_j))
        
        return height_matrix

        
        