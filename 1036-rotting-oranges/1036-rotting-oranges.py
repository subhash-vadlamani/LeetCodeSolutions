class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        q = deque()
        total_orange_count = 0
        total_rotten_count = 0

        def addOrange(i, j):
            nonlocal total_rotten_count
            if i in range(m) and j in range(n) and grid[i][j] == 1:
                grid[i][j] = 2
                total_rotten_count += 1
                q.append((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    total_rotten_count += 1
                if grid[i][j] != 0:
                    total_orange_count += 1
        
        # print(total_rotten_count)
        # print(total_orange_count)
        min_duration = 0
        if total_rotten_count == 0 and total_orange_count == 0:
            return 0
        elif total_rotten_count == 0:
            return -1 
        elif total_rotten_count == total_orange_count:
            return 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                addOrange(x + 1, y)
                addOrange(x - 1, y)
                addOrange(x, y + 1)
                addOrange(x, y - 1)
            min_duration += 1
            print("{} mins & {} rotten oranges".format(min_duration, total_rotten_count))
            if total_rotten_count == total_orange_count:
                break
            
        
        if total_rotten_count == total_orange_count:
            return min_duration
        else:
            return -1


        