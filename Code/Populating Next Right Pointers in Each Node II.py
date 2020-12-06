"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:                                #If root is none, return none.
            return root
        q = [root]                                  #Add root to the initial queue.
        while q:                                    #BFS.
            newq = []                               #Initialize q of next iteration.
            for i in range(len(q)):
                if i < len(q) - 1:                  #Populate next right pointer of current node.
                    q[i].next = q[i + 1]
                if q[i].left is not None:           #If left child is not none, add it to new queue.
                    newq.append(q[i].left)
                if q[i].right is not None:          #If right child is not none, add it to new queue.
                    newq.append(q[i].right)
            q = newq                                #Replace queue with new queue.
        return root                                 #Return root.
