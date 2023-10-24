# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        invalidNodeValue = None
        while q:                                                  #BFS to find the invalid node value.
            newq = []
            childMap = {}                                         #Store the child node value by parent node value.
            for x in q:
                if x.val in childMap:                             #If current node valie is in map, current node is pointed by the invalid node.
                    invalidNodeValue = childMap[x.val]            #Get the invalid node value.
                    break
                if x.left:
                    newq.append(x.left)
                    childMap[x.left.val] = x.val
                if x.right:
                    newq.append(x.right)
                    childMap[x.right.val] = x.val
            q = newq
        q = [root]
        while q:                                                  #BFS to remove invalid node.
            newq = []
            for x in q:
                if x.left:
                    if x.left.val == invalidNodeValue:            #If left child of current node is invalid node, set left child to none.
                        x.left = None
                        return root
                    newq.append(x.left)
                if x.right:
                    if x.right.val == invalidNodeValue:           #If right child of current node is invalid node, set right child to none.
                        x.right = None
                        return root
                    newq.append(x.right)
            q = newq
        return root
