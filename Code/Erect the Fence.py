class Solution:
    def orientation(self, p: List[int], q: List[int], r: List[int]) -> bool:                                    #Given point p, q, r, return if r is on the right of line of p and q.
        return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0]) < 0                                #Calculate the cross product of vector pq and vector qr, and return if it's smaller than 0.

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        leftBottom = min(trees)                                                                                 #Get the left bottom tree.
        treesBySlope = defaultdict(list)
        for t in trees:                                                                                         #Group trees by the slope from each tree to the left bottom tree.
            if t == leftBottom:                                                                                 #If current tree is the left bottom one, skip.
                continue
            treesBySlope[atan2(t[1] - leftBottom[1], t[0] - leftBottom[0])].append(t)
        
        orderedTrees = []                                                                                       #Reorder the trees for traverse.
        maxSlope = max(treesBySlope) if treesBySlope else 0                                                     #Get the max slope if treesBySlope is not empty.
        for k in sorted(treesBySlope):                                                                          #Traverse the sorted keys of treesBySlope.
            treesBySlope[k].sort(key = lambda p: (p[0] - leftBottom[0]) ** 2 + (p[1] - leftBottom[1]) ** 2)     #Sort trees of each slope by the distatnce of the tree to left bottom tree.
            if k == maxSlope and trees:                                                                         #If it's the last slope and trees are not empty, it is the closing segment of fence, we have to reverse the order.
                treesBySlope[k].reverse()
            orderedTrees.extend(treesBySlope[k])                                                                #Add treesBySlope[k] to orderedTrees.

        stack = [leftBottom]                                                                                    #Initialize a stack to start traverse from left bottom tree.
        for t in orderedTrees:                                                                                  #Traverse orderedTrees.
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], t):                                 #While there are at least 2 trees in stack, and the current tree is on the right side of vector from stack[-2] to stack[-1], pop stack to update convex hull.
                stack.pop()
            stack.append(t)                                                                                     #Append current tree to stack.
        return stack                                                                                            #Return stack.
