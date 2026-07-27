# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDist = 0 
    
        def dfs(root):
            nonlocal maxDist 

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            maxDist = max(left+right, maxDist)
            return 1 + max(left, right)
        dfs(root)
        return maxDist