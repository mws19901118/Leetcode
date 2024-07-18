# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def traverse(node: TreeNode) -> (Counter, int):                                            #Traverse subtree to return the count of leaf nodes in subtree by its distance from subtree root, also return the total pairs.
            count, pairs = Counter(), 0                                                            #Initialize counter and pairs.
            if not node.left and not node.right:                                                   #If node is leaf, set count[0] to 1.
                count[0] = 1
            elif (node.left and not node.right) or (not node.left and node.right):                 #If node only has one child, recursively visit that child.
                childCounter, pairs = traverse(node.left if node.left else node.right)             #Pairs equals to pairs from child.
                for x in childCounter:                                                             #For each leaf node under child, its new distance to subtree root has to increase by 1,
                    count[x + 1] = childCounter[x]
            else:                                                                                  #If node has both children, recursively visit them.
                leftCounter, leftPairs = traverse(node.left)
                rightCounter, rightPairs = traverse(node.right)
                pairs = leftPairs + rightPairs                                                     #Each pair in children will also be a [air for parent.
                for x in leftCounter:                                                              #Traverse left counter.
                    count[x + 1] += leftCounter[x]                                                 #For each leaf node under left child, its new distance to subtree root has to increase by 1,
                    for y in range(distance - 1 - x):                                              #If the leaf node under left child whose distance is x, each leaf nodes under right child whose distance is betwen 0 and distance - x - 2 inclusively will make a pair.
                        pairs += leftCounter[x] * rightCounter[y]                                  #So, add leftCounter[x] * rightCounter[y] to pairs.
                for x in rightCounter:                                                             #Traverse right counter.
                    count[x + 1] += rightCounter[x]                                                #For each leaf node under right child, its new distance to subtree root has to increase by 1,
            return count, pairs
        
        return traverse(root)[1]                                                                   #Traverse from root and return the pairs.
