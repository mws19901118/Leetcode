# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):                                                            #Dfs under current node. Return the difference between coins and nodes and the number of necessary moves.
        if root == None:                                                            #If current node is none, return both 0.
            return (0, 0)
        l = self.dfs(root.left)                                                     #Dfs left child.
        r = self.dfs(root.right)                                                    #Dfs right child.
        return (l[0] + r[0] + root.val - 1, l[1] + r[1] + abs(l[0]) + abs(r[0]))    #The difference between coins and nodes in the tree equals that of left child(l[0]) plus that of right child{r[0] plus that of current node(root.val - 1). 
                                                                                    #No matter if left child lacks l[1] coins or needs to give out l[1] coins, there must be l[1] moves between left child and current node.
                                                                                    #The same goes to right child.
                                                                                    #So, the necessary moves is l[1] + r[1] + abs(l[0]) + abs(r[0]).
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[1]                                                    #Dfs from root node and return result.
