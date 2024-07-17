# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        current_array_length = len(nums)
        if not current_array_length:
            return None
        if current_array_length == 1:
            return TreeNode(val=nums[0])
        root = TreeNode(val=nums[current_array_length//2])

        root.left = self.sortedArrayToBST(nums[:current_array_length//2])
        root.right = self.sortedArrayToBST(nums[(current_array_length//2) + 1 : ])

        return root
        