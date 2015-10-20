# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def transform(num,start,end,node):
    mid=(start+end)/2
    node.val=num[mid]
    if start<mid:
        node.left=TreeNode(-1)
        transform(num, start, mid-1, node.left)
    if end>mid:
        node.right=TreeNode(-1)
        transform(num, mid+1, end, node.right)
        
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head==None:
            return None
        num=[]
        while head!=None:                               #Covert the linked list to an array, then deal with the array in the same way as Convert Sorted Array to Binary Search Tree.
            num.append(head.val)
            head=head.next
        length=len(num)
        root=TreeNode(-1)
        transform(num, 0, length-1, root)
        return root
