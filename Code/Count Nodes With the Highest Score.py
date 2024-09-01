class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        adjacentList = defaultdict(list)
        root = -1
        for i, x in enumerate(parents):                                                                    #Traverse parents to build adjacent list and find the root node.
            if x == -1:
                start = i
            else:
                adjacentList[x].append(i)
        score = [0] * len(parents)                                                                         #Initialize score for each node.
        
        def dfs(x: int) -> int:                                                                            #DFS the binary tree to return subtree node count.
            subtreeNodeCount = [dfs(y) for y in adjacentList[x]]                                           #DFS each child to get the subtree node count.
            score[x] = prod(subtreeNodeCount) * max(1, (len(parents) - 1 - sum(subtreeNodeCount)))         #Calculate score: each subtree will be independent, also a tree for the rest of binary tree(edge case is root, which has no parent; but the product cannot be 0, so use 1 instead).
            return sum(subtreeNodeCount) + 1                                                               #Return current subtree node count.
        
        dfs(root)                                                                                          #DFS from root node.
        maxScore = max(score)                                                                              #Find the max score.
        return sum(int(x == maxScore) for i, x in enumerate(score))                                        #Count nodes whose score are max score.
