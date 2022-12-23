"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def postorder_trav(node):
            if len(node)>0:
                for child in node:
                    postorder_trav(child.children)
                    res.append(child.val)
        postorder_trav(root.children)
        res.append(root.val)
        return res