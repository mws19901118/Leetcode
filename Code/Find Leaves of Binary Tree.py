# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []                                                                     #Initialize the result list.

        def traverse(root: Optional[TreeNode]) -> int:                                  #Traverse node and return the its max distance from a leaf node in its subtree.
            if not root:                                                                #If root is none, return -1.
                return -1
            distance = max(traverse(root.left), traverse(root.right)) + 1               #Calculate the disance, which is max of distance of left child and right child plus 1.
            if distance == len(result):                                                 #If current distance equals the length of result, append an empty list to result.
                result.append([])
            result[distance].append(root.val)                                           #Append root.val to result[distance].
            return distance

        traverse(root)                                                                  #Traverse from root.
        return result                                                                   #Return result.
