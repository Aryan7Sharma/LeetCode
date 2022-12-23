"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        def p_trav(child):
            if len(child)>0:
                for i in child:
                    res.append(i.val)
                    p_trav(i.children)
        p_trav(root.children)
        return res