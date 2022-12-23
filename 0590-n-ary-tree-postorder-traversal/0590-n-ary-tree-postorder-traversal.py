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
        def postorder_trav(child):
            if len(child)>0:
                for i in child:
                    postorder_trav(i.children)
                    res.append(i.val)
        postorder_trav(root.children)
        res.append(root.val)
        return res