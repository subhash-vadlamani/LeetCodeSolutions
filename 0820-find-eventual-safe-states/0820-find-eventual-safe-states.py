class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        numCourses = len(graph)
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            
            states[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True
        
        answer = []
        for i in range(numCourses):
            if dfs(i):
                answer.append(i)
        return answer

            

        