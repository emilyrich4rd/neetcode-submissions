# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # logically, it is the rightmost node at every level
        # assuming we go back to the binary search levels idea where we process all the nodes on that level, but we only add to the list whatever's rightmost
        if not root:
            return []
        nodes = []
        queue = [root]
        while len(queue) != 0:
            qlen = len(queue)
            right_child = queue[-1]
            for i in range(qlen):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            for i in range(qlen):
                queue.pop(0)
            nodes.append(right_child.val)
        return nodes
            
