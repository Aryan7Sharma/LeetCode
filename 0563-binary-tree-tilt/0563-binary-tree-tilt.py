# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt_sum = 0
        def dfs(node):
            nonlocal tilt_sum
            if not node:
                return 0
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            tilt = abs(left_node-right_node)
            tilt_sum+=tilt
            
            return left_node+right_node+node.val
        dfs(root)
        return tilt_sum