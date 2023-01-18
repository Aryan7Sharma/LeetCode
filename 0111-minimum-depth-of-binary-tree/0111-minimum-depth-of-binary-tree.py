# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #BFS
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        bfs_queue = deque([(root,1)])
        while bfs_queue:
            curr_node,num = bfs_queue.popleft()
            if not curr_node.left and not curr_node.right:
                return num
            if curr_node.left:
                bfs_queue.append((curr_node.left, num+1))
            if curr_node.right:
                bfs_queue.append((curr_node.right, num+1))
        return -1
        