class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_req_dict = {i:[] for i in range(numCourses)}

        for entry in prerequisites:
            pre_req_dict[entry[0]].append(entry[1])
        
        visited_node_set = set()
        recursion_stack_set = set()
        course_order = []

        def dfs(course):
            if course in recursion_stack_set:
                return False
            if course in visited_node_set:
                return True
            
            recursion_stack_set.add(course)

            for pre_req in pre_req_dict[course]:
                if not dfs(pre_req):
                    return False
            
            recursion_stack_set.remove(course)
            visited_node_set.add(course)
            course_order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return course_order