# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # if there is more node return 0 for sum 
        if not root:
            return 0
        
        #if root has a value less than low then there is no need to check on left side
        # because then all node value of the left subtree  must be less than low 
        if root.val<low:
            return self.rangeSumBST(root.right, low, high)
        
         #if root has a value greater than high then there is no need to check on right side
        # because then all node value of the right subtree must be greater than high
        elif root.val>high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        