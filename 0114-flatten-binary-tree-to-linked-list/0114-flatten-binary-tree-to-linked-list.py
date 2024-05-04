class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Gather all nodes values in a pre-order traversal
        nodes = []
        self.pre_order_traversal(root, nodes)
        
        # Start from the first node and rearrange pointers
        iter_node = root
        for i in range(1, len(nodes)):
            if iter_node:
                iter_node.left = None  # Ensure the left child is None
                iter_node.right = TreeNode(nodes[i])  # Create a new node on the right
                iter_node = iter_node.right  # Move to the next node in the list

    def pre_order_traversal(self, node, nodes):
        if not node:
            return
        nodes.append(node.val)  # Append current node's value
        self.pre_order_traversal(node.left, nodes)  # Traverse left subtree
        self.pre_order_traversal(node.right, nodes)  # Traverse right subtree
