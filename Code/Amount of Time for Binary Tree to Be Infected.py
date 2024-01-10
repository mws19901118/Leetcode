# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacentList = defaultdict(list)                                                      #Store the adjacent list of each node.
        def traverse(curr: Optional[TreeNode], prev: Optional[TreeNode]) -> None:             #Traverse the binary tree to convert it to an undirected graph.
            if not curr:                                                                      #If current node is none, return.
                return
            if prev:                                                                          #If it has a previous node, add an edge between curr and prev.
                adjacentList[curr.val].append(prev.val)
                adjacentList[prev.val].append(curr.val)
            traverse(curr.left, curr)                                                         #Traverse the left subtree.
            traverse(curr.right, curr)                                                        #Traverse the right subtree.

        traverse(root, None)                                                                  #Convert.
        count = 0
        q = set([start])
        visited = set([start])
        while q:                                                                              #BFS to find the longest distance from start to edge.
            newq = set()
            for x in q:
                for y in adjacentList[x]:
                    if y not in visited:
                        newq.add(y)
            visited |= newq
            q = newq
            count += 1
        return count - 1
