"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pAncesters = set()                      #Store the values of ancesters of p.
        curr = p
        while curr:                             #Populate all values of ancesters of p.
            pAncesters.add(curr.val)
            curr = curr.parent
        curr = q
        while curr:                             #Traverse q up.
            if curr.val in pAncesters:          #If curr.val is in pAncesters, curr is the LCA of p and q.
                return curr
            curr = curr.parent
