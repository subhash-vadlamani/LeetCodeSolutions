class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = prerequisites
        g = defaultdict(list)
        for a, b in courses:
            g[a].append(b)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses
        visit_stack = []

        def dfs(i):
            state = states[i]
            if state == VISITED:
                return True
            if state == VISITING:
                return False
            
            states[i] = VISITING
            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED
            visit_stack.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return visit_stack
        