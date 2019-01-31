# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def dfs(root, i, j):                                                                                    #DFS to check if each node is validly able to transform to voyage[i:j].
            if root is None:                                                                                    #If root is node, then only i == j is valid.
                return i == j
            elif root.val != voyage[i]:                                                                         #If the value in root node not equals the value in voyage[i], then no it's not able to transform to voyage.
                return False
            elif root.left is None and root.right is None:                                                      #If root is leaf node, then only i + 1 == j is valid.
                return j - i == 1
            elif root.left is not None and root.right is None:                                                  #If root only has left child, DFS left child and voyage[i + 1:j].
                return dfs(root.left, i + 1, j)
            elif root.left is None and root.right is not None:                                                  #If root only has right child, DFS right child and voyage[i + 1:j].
                return dfs(root.right, i + 1, j)
            else:
                if root.left.val == voyage[i + 1]:                                                              #If root has both child. Then, if the value of left child equals voyage[i + 1], there is no need to flip.
                    rightChildIndex = indexes[root.right.val]                                                   #Find the index of where right child starts in voyage.
                    return dfs(root.left, i + 1, rightChildIndex) and dfs(root.right, rightChildIndex, j)       #Keep DFS left child and right child.
                elif root.right.val == voyage[i + 1]:                                                           #Then, if the value of right child equals voyage[i + 1], we must flip to transform to voyage.
                    result.append(root.val)                                                                     
                    leftChildIndex = indexes[root.left.val]                                                     #Find the index of where left child starts in voyage.
                    return dfs(root.right, i + 1, leftChildIndex) and dfs(root.left, leftChildIndex, j)         #Keep DFS left child and right child.
                else:
                    return False                                                                                #If neither value of left child nor value of right child equals voyage[i + 1], then no it's not able to transform to voyage.
                
        result = []
        indexes = {}                                                                                            #Use a dict to store the index of each value in voyage.
        for i, x in enumerate(voyage):
            indexes[x] = i
        if dfs(root, 0, len(voyage)):                                                                           #DFS from root node. If result is true, return result.
            return result
        else:                                                                                                   #Otherwise, return [-1].
            return [-1]
