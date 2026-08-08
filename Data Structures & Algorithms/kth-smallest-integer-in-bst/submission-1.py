# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # easiest way would be to do in order traversal then count from end
        nodes = []
        def dfs(node):
            if not node:
                return 
            else:
                dfs(node.left)
                nodes.append(node.val)
                dfs(node.right)
        dfs(root.left)
        nodes.append(root.val)
        dfs(root.right)
        print(nodes)
        return nodes[k-1]
