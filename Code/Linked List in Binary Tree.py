# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPathHelper(self, node, root, isLinkedListHead):                                                                                        #Helper function to carry the information whether current linked list node is the head of original linked list during recursion.
        if node is None:                                                                                                                            #If linked list head is none, we have finished recursion for the linked list and found a subpath in tree, return true.
            return True
        if root is None:                                                                                                                            #If linked list head is not none but tree root is none, we can't do recursion anymore, so return false.
            return False
        if isLinkedListHead:                                                                                                                        #If current linked list node is linked list head, we check if linked list node value equals tree root value.
            subPathStartsHere = False
            if node.val == root.val:                                                                                                                #If so, do recursion for the next node in linked list and left child and right child of tree root respectively, and get the OR result of them.
                subPathStartsHere = self.isSubPathHelper(node.next, root.left, False) or self.isSubPathHelper(node.next, root.right, False)
            if subPathStartsHere is True:                                                                                                           #If result is true, subpath starts here so return true.
                return True
            else:                                                                                                                                   #Otherwise, do recursion for the current node in linked list and left child and right child of tree root respectively, and return the OR result of them. 
                return self.isSubPathHelper(node, root.left, True) or self.isSubPathHelper(node, root.right, True)
        else:
            if node.val != root.val:                                                                                                                #If current linked list node is not linked list head, check if linked list node value equals tree root value. If not equal, return false directly. 
                return False
            return self.isSubPathHelper(node.next, root.left, False) or self.isSubPathHelper(node.next, root.right, False)                          #Otherwise, do recursion for the next node in linked list and left child and right child of tree root respectively, and return the OR result of them.

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        return self.isSubPathHelper(head, root, True)
