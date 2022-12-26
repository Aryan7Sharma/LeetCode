# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        def dfs(node, string):
            if node:
                if not node.left and not node.right:
                    string+=str(node.val)
                    self.res.append(string)
                else:
                    string+=str(node.val) + "->"
                dfs(node.left, string)
                dfs(node.right, string)
        dfs(root, "")
        return self.res
        