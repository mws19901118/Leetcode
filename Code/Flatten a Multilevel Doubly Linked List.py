"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        tail = head                               #Use tail to represent the tail of flattened double linked list.
        stack = []                                #Use stack to store the next node of node has child node.
        while tail:                               #While tail is not none.
            while not tail.child and tail.next:   #Whild tail does not have child and tail has next, move tail to next.
                tail = tail.next
            if tail.child:                        #If tail has child.
                if tail.next:                     #If tail still has next, push next to stack and cut the link between tail and next.
                    tail.next.prev = None
                    stack.append(tail.next)
                tail.next = tail.child            #Replace next with child, and remove child.
                tail.next.prev = tail
                tail.child = None
            else:                                 #Otherwise, if stack is not empty, set next to the node popped from stack.
                if stack:
                    tail.next = stack.pop()
                    tail.next.prev = tail
            tail = tail.next                      #Move tail to next.
        return head                               #Return head.
