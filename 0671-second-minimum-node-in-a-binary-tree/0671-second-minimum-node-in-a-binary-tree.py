# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        uniques = set()
        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        minl,ans = root.val,float('inf')
        for v in uniques:
            if minl < v < ans:
                ans = v
        return ans if ans!=float('inf') else -1
                
        
            
    
        