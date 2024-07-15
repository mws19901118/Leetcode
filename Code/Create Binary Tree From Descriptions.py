# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        indegree, adjacentList = defaultdict(int), defaultdict(list)        #Initialize indegree and adjacent list.
        for p, c, isLeft in descriptions:                                   #Populate indegree and adjacent list.
            indegree[c] += 1
            adjacentList[p].append((c, isLeft))
        rootValue = [x for x in adjacentList if not indegree[x]][0]         #Find root value, whose indegree is 0.
        root = TreeNode(rootValue, None, None)                              #Initialize root.
        q = [root]
        while q:                                                            #BFS to build tree.
            newq = []
            for x in q:
                for y, isLeft in adjacentList[x.val]:
                    nextNode = TreeNode(y, None, None)
                    if isLeft:
                        x.left = nextNode
                    else:
                        x.right = nextNode
                    newq.append(nextNode)
            q = newq
        return root
