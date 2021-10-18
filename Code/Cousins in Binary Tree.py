# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [root]                                              #Initialize the q.
        while level:                                                #BFS each level of binary tree.
            nextLevel = []                                          #Initialize the list for next level.
            parent = None                                           #Initialize the parent of x or y for current level.
            for node in level:                                      #Traverse all nodes in level.
                for child in [node.left, node.right]:               #Traverse node.left and node.right.
                    if not child:                                   #If child is none, skip it.
                        continue
                    nextLevel.append(child)                         #Append child to nextLevel.
                    if child.val != x and child.val != y:           #If the value of child is neither x nor y, skip it.
                        continue
                    if not parent:                                  #Now we found a x or y. If parent is none, set parent to node.
                        parent = node
                    elif parent == node:                            #If parent is current node it self, x and y are under one parent node, so they are not cousins, then return false.
                        return False
                    else:                                           #Otherwise, x and y are cousions, then return true.
                        return True
            level = nextLevel                                       #Replace level with nextLevel.
        return False                                                #Return false at last.
