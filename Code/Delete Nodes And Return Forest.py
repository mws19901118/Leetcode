# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteNodes = set(to_delete)                                                                                      #Store to be deleted node values in a set.
        def traverse(node: Optional[TreeNode], isNewRoot: bool) -> List[TreeNode]:                                        #Traverse subtree with a flag indicating if current node is a root and return forest after deleting nodes.
            if not node:                                                                                                  #If node is none, return empty list.
                return []
            result = traverse(node.left, node.val in deleteNodes) + traverse(node.right, node.val in deleteNodes)         #Traverse left subtree and right subtree with correct flag(if delete current node then left child and right child become roots) and combine results.
            if isNewRoot and node.val not in deleteNodes:                                                                 #If current node is root and shouldn't be deleted, append node to result.
                result.append(node)
            if node.left and node.left.val in deleteNodes:                                                                #If left child is not empty and should be deleted, set left child to none.
                node.left = None
            if node.right and node.right.val in deleteNodes:                                                              #If right child is not empty and should be deleted, set right child to none.
                node.right = None
            return result
        
        return traverse(root, True)                                                                                       #Return the result of traversing from root with it is a root.
