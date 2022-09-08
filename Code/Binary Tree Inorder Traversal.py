# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr:                                         #Find the left most leaf and append the path to stack.
            stack.append(curr)
            curr = curr.left
        while stack:                                        #Inorder traverse.
            curr = stack.pop()                              #Pop stack and append value to result.
            result.append(curr.val)
            if curr.right:                                  #If the right child is not none, move to right child.
                curr = curr.right
                while curr:                                 #While curr is not none, append curr to stack and move to left child.
                    stack.append(curr)
                    curr = curr.left
        return result
