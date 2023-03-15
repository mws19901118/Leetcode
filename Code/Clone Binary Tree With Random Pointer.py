# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def copy(root: 'Optional[Node]', rootCopy: 'Optional[NodeCopy]') -> None:                         #Deepcopy node but the random pointer of copied node still points to the random pointer of original node.
            if root.left:
                rootCopy.left = NodeCopy(root.left.val, None, None, root.left.random)
                copy(root.left, rootCopy.left)
            if root.right:
                rootCopy.right = NodeCopy(root.right.val, None, None, root.right.random)
                copy(root.right, rootCopy.right)

        def pointRandomToCopy(root: 'Optional[Node]', rootCopy: 'Optional[NodeCopy]') -> None:            #Point the random pointer of original node to the corresponding copied node.
            if not root or not rootCopy:
                return
            root.random = rootCopy
            pointRandomToCopy(root.left, rootCopy.left)
            pointRandomToCopy(root.right, rootCopy.right)

        def correctRandom(root: 'Optional[Node]', rootCopy: 'Optional[NodeCopy]') -> None:                #If random pointer of copied node is not pointing to none, point it to the random pointer of random pointer, which is the copied random pointer of original node.
            if not root or not rootCopy:
                return
            if rootCopy.random:
                rootCopy.random = rootCopy.random.random
            correctRandom(root.left, rootCopy.left)
            correctRandom(root.right, rootCopy.right)

        if not root:                                                                                      #Return none if root is none.
            return None
        rootCopy = NodeCopy(root.val, None, None, root.random)                                            #Instantiate copied root.
        copy(root, rootCopy)
        pointRandomToCopy(root, rootCopy)
        correctRandom(root, rootCopy)
        return rootCopy                                                                                   #Return copied root.
