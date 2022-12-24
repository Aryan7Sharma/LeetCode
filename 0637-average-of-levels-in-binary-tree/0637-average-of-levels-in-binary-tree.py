# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        count = []
        def average(root, i, sums, count):
            if root:
                if i<len(sums):
                    sums[i]+=root.val
                    count[i]+=1
                else:
                    sums.append(root.val)
                    count.append(1)
                average(root.left, i+1, sums, count)
                average(root.right, i+1, sums, count)
        average(root, 0, sums, count)
        return [sums[i]/count[i] for i in range(len(sums))]
                
        