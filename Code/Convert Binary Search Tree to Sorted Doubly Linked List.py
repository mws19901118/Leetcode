"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(root: 'Optional[Node]') -> ('Optional[Node]', 'Optional[Node]'):        #Traverse the tree and return the head and tail of the double linked list.
            if not root:                                                                     #If root is none, return none and none.
                return None, None
            leftHead, leftTail = traverse(root.left)                                         #Traverse left subtree to get the left head and left tail.
            rightHead, rightTail = traverse(root.right)                                      #Traverse right subtree to get the right head and right tail.
            root.left = leftTail                                                             #Point root.left to left tail.
            if leftTail:                                                                     #If left tail is not none, point its right to root.
                leftTail.right = root
            root.right = rightHead                                                           #Point root.right to right head.
            if rightHead:                                                                    #If right head is not none, point its left to root.
                rightHead.left = root
            head = leftHead if leftHead else root                                            #New head is left head if it is not none, otherwise is root.
            tail = rightTail if rightTail else root                                          #New right is right tail if it is not none, otherwise is root.
            return head, tail                                                                #Return new head and tail.
        
        if not root:                                                                         #If root is none, return none.
            return None
        head, tail = traverse(root)                                                          #Traverse root to get new head and tail.
        head.left, tail.right = tail, head                                                   #Point the left of head to tail and right of tail to head so the double linked list is circular.                                       
        return head                                                                          #Return head as it points to the smallest value.
