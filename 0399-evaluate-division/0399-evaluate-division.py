class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        # Graph construction

        graph = {}

        for i in range(0, len(equations)):
            current_equation_list = equations[i]
            current_equation_evaluation_value = values[i]

            if current_equation_list[0] not in graph:
                graph[current_equation_list[0]] = {}
            
            if current_equation_list[1] not in graph:
                graph[current_equation_list[1]] = {}

            
            graph[current_equation_list[0]][current_equation_list[1]] = current_equation_evaluation_value
            graph[current_equation_list[1]][current_equation_list[0]] = 1.0/current_equation_evaluation_value

        
        # Graph construction completed. Bi-directional graph has been created.


        def dfs(execution_stack, graph, destination, current_answer, visited):
            if not execution_stack:
                return -1.0

            current_element = execution_stack.pop()
            if current_element not in graph:
                return -1.0

            if current_element == destination:
                return current_answer

            current_element_connection_nodes = graph[current_element].keys()

            for element in current_element_connection_nodes:
                if element not in visited:
                    execution_stack.append(element)
                    visited.add(element)

                    current_dfs_answer = dfs(execution_stack, graph, destination, current_answer * graph[current_element][element], visited)

                    if current_dfs_answer != -1.0:
                        return current_dfs_answer
                    else:
                        continue
            return -1.0

        output_array = []

        for element in queries:
            visited_set = set()
            visited_set.add(element[0])
            element_answer = dfs([element[0]], graph, element[1], 1, visited_set)
            output_array.append(element_answer)

        return output_array

            


