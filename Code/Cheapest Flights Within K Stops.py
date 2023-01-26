class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacentList = collections.defaultdict(list)                                                        #Initialize the adjacent list.
        for x, y, p in flights:                                                                             #Build adjacent list with edge weight.
            adjacentList[x].append((y, p))
        minCost, minStop = [float('inf')] * n, [n] * n                                                      #Initialize the minCost and minStop to reach each city.
        minCost[src], minStop[src] = 0, 0                                                                   #Both minCost[src] and minStop[stc] is 0.
        q, count = [(src, 0)], 0                                                                            #Initialize queue with src and initial cost 0; also initialize the initial stop count, which is also 0.
        while q and count <= k:                                                                             #Traverse while q is not empty and count is no greater than k.
            newq = []                                                                                       #Initialize new queue.
            for x, cost in q:                                                                               #Traverse each cities in queue with its current cost.
                for y, p in adjacentList[x]:                                                                #Traverse each neighbor of city with flight price.
                    if count < minStop[y] or cost + p < minCost[y]:                                         #If we can either reach neighbor with less stops or less cost, we can push it to new queue with new calculated cost.
                        newq.append((y, cost + p))
                        minCost[y], minStop[y] = min(minCost[y], cost + p), min(minStop[y], count)          #Also update minCost[y] or minStop[y] if necessary.
            q = newq                                                                                        #Replace q with newq.
            count += 1                                                                                      #Increase count.
        return -1 if minCost[dst] == float('inf') else minCost[dst]                                         #If minCost[dst] is still float('inf'), we are not able to reach it within k stop, so return -1; otherwise, return minCost[dst].
