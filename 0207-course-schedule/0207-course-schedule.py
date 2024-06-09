class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_req_dict = {i:[] for i in range(numCourses)}

        for entry in prerequisites:
            pre_req_dict[entry[0]].append(entry[1])
        
        visited_node_set = set()
        recursion_stack_set = set()

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
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


        # for entry in prerequisites:
        #     if entry[0] not in pre_req_dict:
        #         pre_req_dict[entry[0]] = []
            
        #     pre_req_dict[entry[0]].append(entry[1])
        
        # visited_node_set = set()
        # dfs_stack = []


        # pre_req_dict_keys = pre_req_dict.keys()
        # possible_course_set = set()

        # def dfs(pre_req_dict, pre_req_dict_keys,  visited_node_set, dfs_stack):

        #     current_element = dfs_stack.pop()
        #     if current_element not in possible_course_set:
        #         current_element_pre_req_list = pre_req_dict[current_element]

        #         for element in current_element_pre_req_list:
        #             dfs_stack.append(element)
                



        #     for key in pre_req_dict_keys:
        #         if key not in visited_node_set:
        #             dfs_stack.append(key)



        