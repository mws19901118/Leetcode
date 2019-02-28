"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        pointer = head
        while pointer is not None:                                      #Duplicate every node and insert them after the old ones.
            copy = Node(pointer.val, pointer.next, pointer.random)
            pointer.next = copy
            pointer = pointer.next.next
            
        pointer1 = head.next
        pointer2 = head
        while pointer2 is not None:                                     #Set the new node's random pointer to the next node of old node's random pointer.
            if pointer2.random is not None:
                pointer1.random = pointer2.random.next
            pointer2 = pointer2.next.next
            if pointer1.next is not None:
                pointer1 = pointer1.next.next

        newHead = head.next
        pointer1 = head.next
        pointer2 = head
        while pointer1 is not None:                                     #Separate old linked list and new linked list.
            pointer2.next = pointer1.next
            if pointer1.next is not None:
                pointer1.next = pointer1.next.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return newHead
