class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
            Calculate the indegree of each and every node.
            If there exists a single node with an indegree of 0,
            return that node.

            If there exist multiple nodes with an indegree of 0, return -1
        """

        indegree_dict = dict()
        node_set = set(range(n))

        for u, v in edges:
            if v not in indegree_dict:
                node_set.remove(v)
                indegree_dict[v] = 1
            else:
                indegree_dict[v] += 1
        
        if len(indegree_dict.keys()) < n - 1:
            return -1
        return list(node_set)[0]
        

        