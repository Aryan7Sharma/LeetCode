# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def  dfs(node):
            if node:
                yield from dfs(node.left)
                yield from dfs(node.right)
                yield node.val
        return list(dfs(root))