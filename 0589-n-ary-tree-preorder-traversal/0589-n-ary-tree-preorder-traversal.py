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
        def p_trav(node):
            if len(node)>0:
                for child in node:
                    res.append(child.val)
                    p_trav(child.children)
        p_trav(root.children)
        return res