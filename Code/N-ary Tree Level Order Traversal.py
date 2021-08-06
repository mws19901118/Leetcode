"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []                           #Intialize result.
        q = [root] if root else []            #Initalize queue with root if it's not none.
        while q:                              #BFS.
            level, nextq = [], []             #Initialze current level value and queue for next level.
            for x in q:                       #Traverse q.
                level.append(x.val)           #Append x.val to level.
                nextq.extend(x.children)      #Extend x.children to nextq.
            q = nextq                         #Replace q with nextq.
            result.append(level)              #Append level to result.
        return result
