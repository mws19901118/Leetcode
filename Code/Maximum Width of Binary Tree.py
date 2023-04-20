# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = [(root, 0)]                                                     #Put root and its index(starting from 0) in a queue.
        width = 0
        while level:
            nextLevel = []
            for node, index in level:                                           #Tree level order traversal.
                if not node.left:                                               #If the left child of current node is not none, calculate the index of left child and add left child and its index to queue.
                    nextLevel.append((node.left, index * 2))
                if not node.right:                                              #If the right child of current node is not none, calculate the index of right child and add right child and its index to queue.
                    nextLevel.append((node.right, index * 2 + 1))
            width = max(width, level[-1][1] - level[0][1] + 1)                  #Calculate width of current level and update max width.
            level = nextLevel
        return width
