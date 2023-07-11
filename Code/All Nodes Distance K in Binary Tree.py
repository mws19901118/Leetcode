# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path, result = [], []                                                            #Initialize path from root to target and result.
        def DFS(stack: List[int], curr: TreeNode) -> None:                               #DFS to find the path from root to target.
            stack.append(curr)
            if curr == target:
                path.extend(stack)
                return
            if curr.left:
                DFS(stack, curr.left)
            if curr.right:
                DFS(stack, curr.right)
            stack.pop()
        
        def BFS(curr: TreeNode, skip: TreeNode, distance: int) -> None:                  #BFS to populate result if curr node is k distance from target with some nodes to skip.
            if not distance:
                result.append(curr.val)
                return
            if curr.left and curr.left != skip:
                BFS(curr.left, skip, distance - 1)
            if curr.right and curr.right != skip:
                BFS(curr.right, skip, distance - 1)

        DFS([], root)                                                                    #DFS.
        for i in range(len(path)):                                                       #For each node from target to root, BFS to find all k distance nodes in its subtree while skipping nodes on the path.
            BFS(path[-(i + 1)], None if not i else path[-i], k - i)
        return result
