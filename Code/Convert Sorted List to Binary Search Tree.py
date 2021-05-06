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
    def convert(self, values: List[int], start: int, end: int) -> TreeNode:
        if start > end:                                                                                             #If start > end, return none.
            return None
        mid = (start + end) // 2                                                                                    #Get the mid point between start and end.
        return TreeNode(values[mid], self.convert(values, start, mid - 1), self.convert(values, mid + 1, end))      #Construct BST node recursively.
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:                                                                                                 #Store values of sorted list in an array.
            values.append(head.val)
            head = head.next
        return self.convert(values, 0, len(values) - 1)                                                             #Convert sorted array to BST.
