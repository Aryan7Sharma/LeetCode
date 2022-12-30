# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        ans = float('inf')
        def dfs(node):
            nonlocal res
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(root)
        for i in range(len(res)-1):
            ans = min(ans, abs(res[i]-res[i+1]))
        return ans
            