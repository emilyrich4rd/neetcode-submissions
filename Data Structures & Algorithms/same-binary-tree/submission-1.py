# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traceTree(p) == self.traceTree(q)

    def traceTree(self, node):
        if not node:
            return []
        nodeList = [node.val]
        queue = [node]
        while len(queue) > 0:
            newNode = queue.pop(0)
            if newNode.left:
                nodeList.append(newNode.left.val)
                queue.append(newNode.left)
            else:
                nodeList.append(None)
            if newNode.right:
                nodeList.append(newNode.right.val)
                queue.append(newNode.right)
            else:
                nodeList.append(None)
        return nodeList
            
            