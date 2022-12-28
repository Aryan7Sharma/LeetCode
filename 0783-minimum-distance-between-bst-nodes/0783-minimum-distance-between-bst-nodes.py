# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.queue = deque([root])
        self.all_Nvalue = []
        ans = float('inf')
        while self.queue:
            curr_level = self.queue.popleft()
            self.all_Nvalue.append(curr_level.val)
            if curr_level.left:
                self.queue.append(curr_level.left)
            if curr_level.right:
                self.queue.append(curr_level.right)
        self.all_Nvalue.sort()
        for i in range(len(self.all_Nvalue)-1):
            ans = min(ans, self.all_Nvalue[i+1]-self.all_Nvalue[i])
        return ans