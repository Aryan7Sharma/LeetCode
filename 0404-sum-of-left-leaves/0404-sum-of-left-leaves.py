# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    left_leafSum=0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and (root.left.left is None) and (root.left.right is None):
                self.left_leafSum+=root.left.val
            self.sumOfLeftLeaves(root.left)
            self.sumOfLeftLeaves(root.right)
        return self.left_leafSum
        
        