# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                                                                                    #If root is none, return empty list.
            return []
        q = [(root, 0)]                                                                                 #Initialize a queue with root and current column coordinate 0.
        cols = defaultdict(list)                                                                        #Store numbers in each column from top to bottom.
        while q:                                                                                        #BFS.
            newq = []
            for x, i in q:                                                                              #Traverse each node and its column coordinate.
                cols[i].append(x.val)                                                                   #Append the value of current node to its column.
                if x.left:                                                                              #If x.left is not none, append it and its column coordinate to newq.
                    newq.append((x.left, i - 1))
                if x.right:                                                                             #If x.right is not none, append it and its column coordinate to newq.
                    newq.append((x.right, i + 1))
            q = newq                                                                                    #Replace q with newq.
        return [cols[i] for i in range(min(cols.keys()), max(cols.keys()) + 1)]                         #Return each column from the min column coordinate to max column coordinate. It's guaranteed to be consecutive, because 2 nodes cannot be connected in 2 columns whose gap is greater than 1.
