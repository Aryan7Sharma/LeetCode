# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float('inf')
        def dfs(node, num):
            if node:
                if not node.left and not node.right:
                    self.min_depth = min(self.min_depth, num)
                dfs(node.left, num+1)
                dfs(node.right, num+1)
        dfs(root, 1)
        return self.min_depth
        