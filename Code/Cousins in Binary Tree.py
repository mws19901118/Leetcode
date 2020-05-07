# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = set([root])
        while level:                                                                                #BFS each level of binary tree.
            foundX, foundY = False, False
            nextLevel = set()
            for node in level:
                if node.left is not None:
                    nextLevel.add(node.left)
                    foundX |= node.left.val == x and (node.right is None or node.right.val != y)    #If left child is x, foundX is true only if right child is none or right child is not y.
                    foundY |= node.left.val == y and (node.right is None or node.right.val != x)    #If left child is y, foundX is true only if right child is none or right child is not z.
                if node.right is not None:
                    nextLevel.add(node.right)
                    foundX |= node.right.val == x and (node.left is None or node.left.val != y)     #If right child is x, foundX is true only if left child is none or left child is not y.
                    foundY |= node.right.val == y and (node.left is None or node.left.val != x)     #If right child is y, foundX is true only if left child is none or left child is not x.
            if foundX and foundY:                                                                   #If found both x and y, return true.
                return True
            level = nextLevel
        return False
