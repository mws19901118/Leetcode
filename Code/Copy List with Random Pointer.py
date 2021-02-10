"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        while curr:                                                                 #Duplicate every node and insert them after the old ones.
            curr.next = Node(curr.val, curr.next, None)
            curr = curr.next.next
        curr = head
        while curr:                                                                 #Set the new node's random pointer to the next node of old node's random pointer if old node's random pointer is not none.
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        dummyHead = Node(0, head, None)
        curr = dummyHead
        while curr.next:                                                            #Separate old linked list and new linked list.
            curr.next = curr.next.next
            curr = curr.next
        return dummyHead.next
