# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool: # Byusing DFS Method
        self.uniVal = root.val
        dfs_queue = deque([root])
        while dfs_queue:
            curr_level = dfs_queue.popleft()
            if curr_level.val!=self.uniVal:
                return False
            if curr_level.left:
                dfs_queue.append(curr_level.left)
            if curr_level.right:
                dfs_queue.append(curr_level.right)
        return True