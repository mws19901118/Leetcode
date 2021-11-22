# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:                                                    #If root is none, return none.
            return None
        if root.val < key:                                              #If key is in right subtree, delete node in right subtree and update right child.
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:                                            #If key is in left subtree, delete node in left subtree and left right child.
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:                        #If root value is key and root has no child, delete it and set root to none.
                root = None
            elif not root.left and root.right:                          #If root value is key and root only has right child, subsitute root with its right child.
                root = root.right
            elif root.left and not root.right:                          #If root value is key and root only has left child, subsitute root with its left child.
                root = root.left
            else:                                                       #Otherwise, root value is key and root has both children.
                l = root.left
                while l.right is not None:                              #Find the right most node in left subtree.
                    l = l.right
                root.val, l.val = l.val, root.val                       #Swap its value with root value.
                root.left = self.deleteNode(root.left, key)             #Delete node in left subtree.
        return root                                                     #Return root.
