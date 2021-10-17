# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, target: int, cumsum: int, count: dict) -> int:
        if not node:                                                    #If root is none, return.
            return 0
        cumsum += node.val                                              #Calculate the cumulative sum from root to current node.
        result = count[cumsum - target]                                 #Add count[cumsum - target] to result, because if there is a node whose cumulative sum is cumsum - target, the path sum from that node(not inclusive) to current node equals target.  
        count[cumsum] += 1                                              #Add the count of cumulative sum to dictionary.
        result += self.dfs(node.left, target, cumsum, count)            #DFS in left child.
        result += self.dfs(node.right, target, cumsum, count)           #DFS in left child.
        count[cumsum] -= 1                                              #Reduce the count of cumulative sum.
        return result

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = defaultdict(int)                                        #Use a dictionary to count the appearance during DFS.
        count[0] = 1                                                    #Inially, it's 0.
        return self.dfs(root, targetSum, 0, count)                      #Return the result after DFS.
