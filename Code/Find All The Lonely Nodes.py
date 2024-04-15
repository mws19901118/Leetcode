# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []                                                                            #Initialize result.
        def traverse(curr: Optional[TreeNode], prev: Optional[TreeNode]) -> None:              #Traverse the tree.
            if not curr:                                                                       #If current node is none, return.
                return
            if prev and not (prev.left and prev.right):                                        #If it has parent and parent only has one child, append the value of current node to result.
                result.append(curr.val)
            traverse(curr.left, curr)                                                          #Traverse left subtree.
            traverse(curr.right, curr)                                                         #Traverse right subtree.

        traverse(root, None)                                                                   #Traverse from root with no parent.
        return result
