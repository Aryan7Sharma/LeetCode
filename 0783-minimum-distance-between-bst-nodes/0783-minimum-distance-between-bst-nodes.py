# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int: #DFS
        self.all_Nvalue = []
        ans = float('inf')
        def dfs(node):
            if node:
                dfs(node.left)
                self.all_Nvalue.append(node.val)
                dfs(node.right)
        dfs(root)
        for i in range(len(self.all_Nvalue)-1):
            ans = min(ans, self.all_Nvalue[i+1]-self.all_Nvalue[i])
        return ans