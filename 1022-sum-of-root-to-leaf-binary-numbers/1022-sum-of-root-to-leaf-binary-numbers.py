# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        leaf_sum = 0
        def preOrder(node, curr_val):
            nonlocal leaf_sum
            if node:
                curr_val = (curr_val<<1)|node.val
                if (not node.left and not node.right):
                    leaf_sum+=curr_val
                preOrder(node.left, curr_val)
                preOrder(node.right, curr_val)
        preOrder(root, 0)
        return leaf_sum
        