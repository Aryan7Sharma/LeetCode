# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.curr = TreeNode()
        def inOrder(node):
            if node:
                inOrder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inOrder(node.right)
        inOrder(root)
        return ans.right
                