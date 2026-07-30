# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if root and not subRoot:
            return False
        if self.sameTree(root, subRoot):
            return True
        else:
            if not root:
                return False
            else:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root2 and root1) or (not root1 and root2) or root1.val != root2.val:
            return False
        else:
            return (self.sameTree(root1.right, root2.right)) and (self.sameTree(root1.left, root2.left))
        
