from collections import defaultdict
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
            Directed graph. Each node has at most one outgoing edge.

            graph is represented with a 0-indexed array.

            two integers 'node1' and 'node2' given

            Return the index of the node that cn be reached from both 'node1' and 'node2',
            such that the maximum between the distance from 'node1' to that node, and 'node2' to that node
            is minimized
        """

        """
            Do BFS on node1 and node2 and store the minimum distance to reach each node, -1 if impossible.
            since cycles are possible, maintain a vist set
        """
        number_of_nodes = len(edges)

        def bfs(start_node, graph):
            """
            Return a list where idx = node, value = shortest distance from
            start_node (-1 if unreachable).
            """
            dist = [-1] * number_of_nodes
            q = deque([(start_node, 0)])
            visited = set()

            while q:
                u, d = q.popleft()
                if u in visited:        # avoid re-processing in cycles
                    continue
                visited.add(u)
                dist[u] = d
                for v in graph.get(u, []):
                    if v not in visited:
                        q.append((v, d + 1))
            return dist

        # def bfs(start_node, graph):
        #     """
        #         returns a dict where each key is the node number, corresponding value is the
        #         minimum hops needed to get to that node from the start node.
        #     """

        #     q = deque()
        #     q.append((start_node, 0)) # (node, distance_from_start_node)
        #     visit = set()
        #     min_distance_dict = dict()
        #     for i in range(number_of_nodes):
        #         min_distance_dict[i] = -1
        #     # min_distance_dict[start_node] = 0
        #     while q:
        #         current_node, current_distance = q.popleft()
        #         min_distance_dict[current_node] = current_distance
        #         visit.add(current_node)

        #         for new_node in graph.get(current_node, []):
        #             if new_node not in visit:
        #                 q.append((new_node, current_distance + 1))
            
        #     return min_distance_dict


        # build adj list
        graph = defaultdict(list)
        for i in range(number_of_nodes):
            if edges[i] != -1:
                graph[i].append(edges[i])
        
        d1 = bfs(node1, graph)
        d2 = bfs(node2, graph)

        best_max = float("inf")   # we want to MINIMIZE this value
        best_idx = -1

        for i in range(number_of_nodes):
            if d1[i] != -1 and d2[i] != -1:           # reachable from both
                candidate = max(d1[i], d2[i])         # larger of the two paths
                # strictly smaller max-distance, or same distance but smaller index
                if candidate < best_max or (candidate == best_max and i < best_idx):
                    best_max = candidate
                    best_idx = i

        return best_idx

        # print(f"node1_min_distance_dict : {node1_min_distance_dict}")
        # print(f"node2_min_distance_dict: {node2_min_distance_dict}")

        # current_max = float('-inf')
        # current_max_index = float('-inf')

        # for i in range(number_of_nodes):
        #     if node1_min_distance_dict[i] != -1 and node2_min_distance_dict[i] != -1:
        #         potential_max = max(node1_min_distance_dict[i], node2_min_distance_dict[i])
        #         if potential_max > current_max:
        #             current_max = potential_max
        #             current_max_index = i
        #     if current_max_index != float('-inf'):
        #         break
            
        # return current_max_index if current_max_index != float('-inf') else -1






        