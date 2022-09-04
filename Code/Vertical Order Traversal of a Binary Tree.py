# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)                                               #Use dict to store the values of each x.
        level = [(root, 0)]                                                 #Current level of pairs of node and x.
        while level:                                                        #BFS each level.
            nextLevel = []                                                  #Next level of pairs of node and x.
            dLevel = defaultdict(list)                                      #Current level's dict to store values of each x.
            for p in level:                                                 #Travese current level.
                if p[0].left:                                               #If current node has left child, add left child to next level with x of left child.
                    nextLevel.append((p[0].left, p[1] - 1))
                if p[0].right:                                              #If current node has right child, add right child to next level with x of right child.
                    nextLevel.append((p[0].right, p[1] + 1))
                dLevel[p[1]].append(p[0].val)                               #Add current node val to current level's dict by x. 
            level = nextLevel                                               #Go to next level.
            for x in dLevel:                                                #Update main dict according to this level's dict.
                d[x].extend(sorted(dLevel[x]))                              #Sort to resolve conflict(values with same x and y).
        return [d[x] for x in range(min(d.keys()), max(d.keys()) + 1)]      #For each x in main dict, append values to result.
