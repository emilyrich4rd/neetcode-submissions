# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, l, u):
            if not node:
                return True
            if not (node.val < u and node.val > l):
                return False
            return helper(node.left, l, node.val) and helper(node.right, node.val, u)
        return helper(root, float("-inf"), float("inf"))