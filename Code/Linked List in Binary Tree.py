# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def traverse(node, root, isLinkedListHead):                                                                                 #Traverse binary tree and linked list simultaneously and carry the information whether current linked list node is the head of original linked list during recursion.
            if not node:                                                                                                            #If linked list head is none, we have finished recursion for the linked list and found a subpath in tree, return true.
                return True
            if not root:                                                                                                            #If linked list head is not none but tree root is none, we can't do recursion anymore, so return false.
                return False
            if isLinkedListHead:                                                                                                    #If current linked list node is linked list head, we check if linked list node value equals tree root value.
                if node.val == root.val and (traverse(node.next, root.left, False) or traverse(node.next, root.right, False)):      #If so, do recursion for the next node in linked list and left child and right child of tree root respectively, and get the OR result of them.
                    return True                                                                                                     #If result is true, subpath starts here so return true.
                else:                                                                                                               #Otherwise, do recursion for the current node in linked list and left child and right child of tree root respectively, and return the OR result of them. 
                    return traverse(node, root.left, True) or traverse(node, root.right, True)
            else:
                if node.val != root.val:                                                                                            #If current linked list node is not linked list head, check if linked list node value equals tree root value. If not equal, return false directly. 
                    return False
                return traverse(node.next, root.left, False) or traverse(node.next, root.right, False)                              #Otherwise, do recursion for the next node in linked list and left child and right child of tree root respectively, and return the OR result of them.
        return traverse(head, root, True)
