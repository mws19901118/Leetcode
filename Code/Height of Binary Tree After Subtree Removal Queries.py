# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth = defaultdict(int)                                                                                        #Store the depth of each node.
        top2HeightPerDepth = defaultdict(list)                                                                          #Store the top 2 heights of nodes per depth.
        
      def traverse(root: Optional[TreeNode], currentDepth: int) -> int:                                                 #Traverse tree.
            if not root:                                                                                                #If root is none, return 0.
                return 0
            
            height = max(traverse(root.left, currentDepth + 1), traverse(root.right, currentDepth + 1))                 #Traverse left child and right child recursively.
            depth[root.val] = currentDepth                                                                              #Store the depth of current node.
            if not top2HeightPerDepth[currentDepth]:                                                                    #Update the top 2 height of nodes at current depth.
                top2HeightPerDepth[currentDepth].append((root.val, height))
            elif len(top2HeightPerDepth[currentDepth]) == 1:
                if top2HeightPerDepth[currentDepth][0][1] < height:
                    top2HeightPerDepth[currentDepth].append(top2HeightPerDepth[currentDepth][0])
                    top2HeightPerDepth[currentDepth][0] = (root.val, height)
                else:
                    top2HeightPerDepth[currentDepth].append((root.val, height))
            elif len(top2HeightPerDepth[currentDepth]) == 2:
                if top2HeightPerDepth[currentDepth][0][1] < height:
                    top2HeightPerDepth[currentDepth][1] = top2HeightPerDepth[currentDepth][0]
                    top2HeightPerDepth[currentDepth][0] = (root.val, height)
                elif top2HeightPerDepth[currentDepth][1][1] < height:
                    top2HeightPerDepth[currentDepth][1] = (root.val, height)
            return height + 1

        getHeight(root, 0)                                                                                              #Traverse from root.
        result = []                                                                                                     #Initialize result.
        for x in queries:                                                                                               #Traverse queires.
            currentDepth = depth[x]                                                                                     #Get the depth of current query.
            if len(top2HeightPerDepth[currentDepth]) == 1:                                                              #If current depth only has one node, the new height is depth - 1.
                result.append(currentDepth - 1)
            elif x == top2HeightPerDepth[currentDepth][0][0]:                                                           #If current node is the node with max height at current depth, the new height is currentDepth plus the second highest height at current depth.
                result.append(currentDepth + top2HeightPerDepth[currentDepth][1][1])
            else:                                                                                                       #Otherwise, the new height is currentDepth plus the highest height at current depth.
                result.append(currentDepth + top2HeightPerDepth[currentDepth][0][1])
        return result                                                                                                   #Return result.
