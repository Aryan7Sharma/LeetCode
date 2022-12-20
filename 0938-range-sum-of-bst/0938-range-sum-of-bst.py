# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sumNode = 0
        def postorder(node):
            if not node:
                return None
            postorder(node.left)
            postorder(node.right)
            if node.val>=low and node.val<=high:
                self.sumNode+=node.val
        
        postorder(root)
        return self.sumNode
        