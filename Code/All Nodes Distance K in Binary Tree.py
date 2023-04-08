# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        distances = {}                                                                                                      #Store the distances of each node on the route from root to target to target.
        def findTarget(root: TreeNode, target: TreeNode):                                                                   #Find the target.
            if not root:                                                                                                    #If root is none, return -1.
                return -1
            if root.val == target.val:                                                                                      #If root is target, set its distance to 0 and return 0.
                distances[root.val] = 0
                return 0
            d = max(findTarget(root.left, target), findTarget(root.right, target))                                          #Get the max distance of left child and right child.
            if d != -1:                                                                                                     #If it's not -1, distance from current root to target is d + 1. Set its distance and return.
                distances[root.val] = d + 1
                return d + 1
            else:                                                                                                           #Otherwise, return -1.
                return -1

        findTarget(root, target)                                                                                            #Find target from root.
        result = []                                                                                                         #Initialize result.
        q = [(root, distances[root.val])]                                                                                   #Initialize queue for BFS with root and the distance from root to target.
        while q:                                                                                                            #BFS.
            newq = []
            for x, d in q:                                                                                                  #Traverse q.
                if d == k:                                                                                                  #If current distance is k, append x.val to result.
                    result.append(x.val)
                if x.left:                                                                                                  #If x has left child, next_d is d + 1 if x.left is not on the route from root to target; otherwise, next_d is distances[x.left.val].
                    next_d = d + 1 if x.left.val not in distances else distances[x.left.val]
                    newq.append((x.left, next_d))                                                                           #Append x.left and next_d to newq.
                if x.right:                                                                                                 #If x has right child, next_d is d + 1 if x.right is not on the route from root to target; otherwise, next_d is distances[x.right.val].
                    next_d = d + 1 if x.right.val not in distances else distances[x.right.val]
                    newq.append((x.right, next_d))                                                                          #Append x.right and next_d to newq.
            q = newq                                                                                                        #Replace q with newq.
        return result                                                                                                       #Return result.
