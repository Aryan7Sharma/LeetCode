# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool: # Byusing BFS Method
        if root:
            print(root.val)
            if root.left and root.val!=root.left.val:
                return False
            if root.right and root.val!=root.right.val:
                return False
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return True