# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        @cache
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        lookup = {}
        def calculate(node, depth, max_other):
            if node is None:
                return

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            if node.left is not None:
                lookup[node.left.val] = max(right_height + depth, max_other)
                calculate(node.left, depth + 1, lookup[node.left.val])
            if node.right is not None:
                lookup[node.right.val] = max(left_height + depth, max_other)
                calculate(node.right, depth + 1, lookup[node.right.val])
        
        calculate(root, 0, 0)

        ans = []
        for q in queries:
            ans.append(lookup[q])
        return ans

            


            
        



        # height = {}
        # excluded_height = {}

        # value_to_node = {}

        # parent = {}

        # def compute_heights(node):
        #     if not node:
        #         return 0
        #     value_to_node[node.val] = node

        #     left_h = compute_heights(node.left)
        #     right_h = compute_heights(node.right)

        #     height[node.val] = 1 + max(left_h, right_h)

        #     if node.left:
        #         parent[node.left.val] = node.val
        #     if node.right:
        #         parent[node.right.val] = node.val
            
        #     return height[node.val]
        # compute_heights(root)

        # def compute_excluded_heights(node, parent_excluded_h):
        #     if not node:
        #         return
            
        #     excluded_height[node.val] = parent_excluded_h

        #     left_h = height[node.left.val] if node.left else -1
        #     right_h = height[node.right.val] if node.right else -1

        #     if node.left:
        #         if node.right:
        #             new_excluded = max(parent_excluded_h, right_h + 1) + 1
        #         else:
        #             new_excluded = parent_excluded_h + 1
        #         compute_excluded_heights(node.left, new_excluded)
        #     if node.right:
        #         if node.left:
        #             new_excluded = max(parent_excluded_h, left_h + 1) + 1
        #         else:
        #             new_excluded = parent_excluded_h + 1
        #         compute_excluded_heights(node.right, new_excluded)
        
        # compute_excluded_heights(root, 0)

        # answer_list = []
        # for query in queries:
        #     if query == root.val:
        #         answer_list.append(-1)
        #     else:
        #         answer_list.append(excluded_height.get(query, 0))
        # return answer_list

        































        # def treeHeight(root):
        #     if not root:
        #         return 0
        #     elif root and (not root.left and not root.right):
        #         return 0
        #     else:
        #         answer = 1 + max(treeHeight(root.left), treeHeight(root.right))
        #         return answer
        
        # def findParentAndNode(root, parent, value_dict):
        #     """
        #         We can design this function to return the parent 
        #         and node value of each value
        #     """

        #     root_value = root.val
        #     value_dict[root_value] = {"root": root, "parent": parent}

        #     if root.left:
        #         findParentAndNode(root.left, root, value_dict)
        #     if root.right:
        #         findParentAndNode(root.right, root, value_dict)
        #     return
        
        # def cloneBinaryTreeDFS(root):
        #     if root is None:
        #         return None
            
        #     new_root = TreeNode(root.val)

        #     new_root.left = cloneBinaryTreeDFS(root.left)
        #     new_root.right = cloneBinaryTreeDFS(root.right)

        #     return new_root
        
        # new_root = cloneBinaryTreeDFS(root)
        # value_dict = dict()
        # findParentAndNode(new_root, None, value_dict)

        # answer_list = []
        # for query in queries:
        #     required_query_parent = value_dict[query]["parent"]
        #     required_query_root = value_dict[query]["root"]
        #     if required_query_parent.left == required_query_root:
        #         required_query_parent.left = None
        #     else:
        #         required_query_parent.right = None
            
        #     current_tree_height = treeHeight(new_root)
        #     answer_list.append(current_tree_height)

        #     new_root = cloneBinaryTreeDFS(root)
        #     value_dict = dict()
        #     findParentAndNode(new_root, None, value_dict)
        # return answer_list
        

        


        