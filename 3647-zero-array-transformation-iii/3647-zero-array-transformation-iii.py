class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = collections.deque(sorted(queries))
        
        good_to_use = []
        currently_using = []
        count = 0

        for index, x in enumerate(nums):
            while len(q) > 0 and q[0][0] <= index:
                heapq.heappush(good_to_use, -q[0][1])
                q.popleft()
            
            # remove expired queries
            while len(currently_using) > 0:
                if currently_using[0] < index:
                    heapq.heappop(currently_using)
                else:
                    break
            # if we need more queries, we take them
            while len(currently_using) < x:
                if len(good_to_use) == 0:
                    return -1
                r = -heapq.heappop(good_to_use)
                if r < index:
                    continue
                heapq.heappush(currently_using, r)
                count += 1
        return len(queries) - count

            
            
           
        
        # print(greedy_queries)
        # def is_zero_array(nums, queries):
        #     N = len(nums)

        #     delta = [0] * (N + 1)

        #     for l, r in queries:
        #         delta[l] += 1
        #         delta[r + 1] -= 1
            
        #     for i in range(1, N + 1):
        #         delta[i] += delta[i - 1]
            
        #     for i in range(N):
        #         if nums[i] > delta[i]:
        #             return False
        #     return True
        
        # if is_zero_array(nums, greedy_queries):
        #     return len(queries) - len(greedy_queries)
        # else:
        #     return -1
        
            

        