# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def distribute(root: Optional[TreeNode]):                                                                         #DFS under current node and return the difference between coins and nodes and the number of necessary moves.
            if not root:                                                                                                  #If current node is none, return both 0.
                return 0, 0
            leftDiff, leftMoves = distribute(root.left)                                                                   #DFS left child.
            rightDiff, rightMmoves = distribute(root.right)                                                               #DFS right child.
            return leftDiff + rightDiff + root.val - 1, leftMoves + rightMmoves + abs(leftDiff) + abs(rightDiff)          #The difference between coins and nodes in the tree equals that of leftDiff + rightDiff + root.val - 1. 
                                                                                                                          #No matter if left child lacks leftMoves coins or needs to give out leftMoves coins, there must be leftMoves moves between left child and current node.
                                                                                                                          #The same goes to right child.
                                                                                                                          #So, the necessary moves is leftMoves + rightMmoves + abs(leftDiff) + abs(rightDiff).
        return distribute(root)[1]                                                                                        #DFS from root node and return result.
