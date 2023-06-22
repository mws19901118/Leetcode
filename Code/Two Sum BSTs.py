# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        root1Stack, root2Stack = [], []                                #Initialize stacks for traversing root1 and root2 respectively.
        while root1.left:
            root1Stack.append(root1)
            root1 = root1.left
        while root2.right:
            root2Stack.append(root2)
            root2 = root2.right
            
        
        while root1:                                                  #Traverse root1 from left to right.
            while root2 and root1.val + root2.val > target:           #While root2 and root1.val + root2.val > target, traverse root2 from right to left.
                if root2.left:
                    root2 = root2.left
                    while root2.right:
                        root2Stack.append(root2)
                        root2 = root2.right
                elif root2Stack:
                    root2 = root2Stack.pop()
                else:
                    root2 = None
            
            if root2 and root1.val + root2.val == target:            #If found 2 sum, return true.
                return True

            if root1.right:                                          #Move root1.
                root1 = root1.right
                while root1.left:
                    root1Stack.append(root1)
                    root1 = root1.left
            elif root1Stack:
                root1 = root1Stack.pop()
            else:
                root1 = None
                                        
        return False                                                 #Return false.
        
