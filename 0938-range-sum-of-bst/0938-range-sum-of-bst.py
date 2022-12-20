# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sumNode = 0
        def preorder(node):
            if not node:
                return None
            elif node.val>=low and node.val<=high:
                self.sumNode+=node.val
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return self.sumNode
        