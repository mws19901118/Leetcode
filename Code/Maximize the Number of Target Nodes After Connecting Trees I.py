class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def countTargetForEachNode(edges: List[List[int]], limit: int) -> Counter:      #Count target for each node given edges and limit.
            adjacentList = defaultdict(list)                                            #Build adjacent list.
            for x, y in edges:
                adjacentList[x].append(y)
                adjacentList[y].append(x)
            count = Counter()                                                           #Initialize counter.
            for i in range(len(edges) + 1):                                             #Traverse each node.
                q = [i]
                visited = set([i])
                length, count[i] = 0, 0
                while length <= limit and q:                                            #BFS while q is not empty and length is not greater than limit.
                    newq = []
                    for x in q:
                        for y in adjacentList[x]:
                            if y in visited:
                                continue
                            newq.append(y)
                            visited.add(y)
                    length += 1                                                         #Increase length after current iteration.
                    count[i] += len(q)                                                  #Add the current length of q to count[i].
                    q = newq
            return count                                                                #Return counter.
        
        count1 = countTargetForEachNode(edges1, k)                                      #Count target for each node in tree1 with k as limit.
        count2 = countTargetForEachNode(edges2, k - 1)                                  #Count target for each node in tree2 with k - 1 as limit.
        maxCount2 = max(count2.values())                                                #Since we can connect to any node in tree2, we just connect to the node with max target.
        return [count1[i] + maxCount2 for i in range(len(edges1) + 1)]                  #Return count1[i] + maxCount2 for each node in tree1.
