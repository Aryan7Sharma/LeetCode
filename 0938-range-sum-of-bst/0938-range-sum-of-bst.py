# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sumNode = 0
        def inOrder(node):
            if not node:
                return None
            inOrder(node.left)
            if node.val>=low and node.val<=high:
                self.sumNode+=node.val
            inOrder(node.right)
        
        inOrder(root)
        return self.sumNode
        