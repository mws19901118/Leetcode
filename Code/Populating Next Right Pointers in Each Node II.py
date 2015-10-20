# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root==None:                          #If tree is empty, return.
            return
        firstnodewithchild=None                 
        while root!=None:
            if firstnodewithchild==None and (root.left!=None or root.right!=None):
                firstnodewithchild=root         #Record the first node in current level that has child.
            if root.left!=None and root.right!=None:
                root.left.next=root.right       #If a node has both left child and right child, then the next pointer of left child points to right child.
            rootnext=None                       #Record next node of right child(or left child if no right child).
            temp=root.next
            while temp!=None and temp.left==None and temp.right==None:        #Search for the nearest "next" node with child
                    temp=temp.next
            if temp!=None:                      #If found, the next pointer of right child(or left child if no right child) points to left child(or right child if no left child) of the nearest "next" node with child.
                if temp.left!=None:
                    rootnext=temp.left
                elif temp.right!=None:
                    rootnext=temp.right
            
                if root.right!=None:
                    root.right.next=rootnext
                elif root.left!=None and root.right==None:
                    root.left.next=rootnext
                
                root=temp                       #Use the nearest "next" node to replace current node.
            
            elif firstnodewithchild!=None:      #If not found, it means that we reach the end of current level. 
                if firstnodewithchild.left!=None:       #If the first node in current level that has child is not empty, use its left child(or right child if no left child) to replace current node.
                    root=firstnodewithchild.left
                    firstnodewithchild=None
                else:
                    root=firstnodewithchild.right
                    firstnodewithchild=None
            else:                                       #If the first node in current level that has child is empty, it means that we have already traverse the whole binary tree and we should end the loop.
                break
