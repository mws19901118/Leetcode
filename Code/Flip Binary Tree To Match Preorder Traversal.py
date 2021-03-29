# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, i: int, j: int, result: List[int], indexes: dict, voyage: List[int]) -> bool:                                                         #DFS to check if each node is validly able to transform to voyage[i:j].
        if root is None:                                                                                                                                                #If root is node, then only i == j is valid.
            return i == j
        if root.val != voyage[i]:                                                                                                                                       #If the value in root node not equals the value in voyage[i], then no it's not able to transform to voyage.
            return False
        
        if root.left is None and root.right is None:                                                                                                                    #If root is leaf node, then only i + 1 == j is valid.
            return j - i == 1
        elif root.left is not None and root.right is None:                                                                                                              #If root only has left child, DFS left child and voyage[i + 1:j].
            return self.dfs(root.left, i + 1, j, result, indexes, voyage)
        elif root.left is None and root.right is not None:                                                                                                              #If root only has right child, DFS right child and voyage[i + 1:j].
            return self.dfs(root.right, i + 1, j, result, indexes, voyage)
        
        if root.left.val == voyage[i + 1]:                                                                                                                              #If root has both child. Then, if the value of left child equals voyage[i + 1], there is no need to flip.
            rightChildIndex = indexes[root.right.val]                                                                                                                   #Find the index of where right child starts in voyage.
            return self.dfs(root.left, i + 1, rightChildIndex, result, indexes, voyage) and self.dfs(root.right, rightChildIndex, j, result, indexes, voyage)           #Keep DFS left child and right child.
        elif root.right.val == voyage[i + 1]:                                                                                                                           #Then, if the value of right child equals voyage[i + 1], we must flip to transform to voyage.
            result.append(root.val)                                                                                                                                     #Append root's value to result.
            leftChildIndex = indexes[root.left.val]                                                                                                                     #Find the index of where left child starts in voyage.
            return self.dfs(root.right, i + 1, leftChildIndex, result, indexes, voyage) and self.dfs(root.left, leftChildIndex, j, result, indexes, voyage)             #Keep DFS left child and right child.
        else:                                                                                                                                                           #If neither value of left child nor value of right child equals voyage[i + 1], then no it's not able to transform to voyage.
            return False
        
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        result = []
        indexes = {x: i for i, x in enumerate(voyage)}                                                                                                                  #Use a dict to store the index of each value in voyage.
        return result if self.dfs(root, 0, len(voyage), result, indexes, voyage) else [-1]                                                                              #DFS from root node. If result is true, return result; #Otherwise, return [-1].
