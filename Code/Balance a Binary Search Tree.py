# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        order = []
        def traverse(root: TreeNode) -> None:                                                          #In-order traversal to convert BST to list.
            if root:
                traverse(root.left)
                order.append(root.val)
                traverse(root.right)
        
        def construct(left: int, right: int) -> TreeNode:                                              #Construct balanced BST from sorted list.
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(order[mid], construct(left, mid - 1), construct(mid + 1, right))
        
        traverse(root)
        return construct(0, len(order) - 1)
