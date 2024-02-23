class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacentList = defaultdict(list)                                                            #Build adjacent list.
        for f, t, p in flights:
            adjacentList[f].append((t, p))
        min_cost = {}                                                                               #Initialize min cost from src to every city.
        q, count = {src: 0}, 0                                                                      #Initialize queue to start from src; also initialize count of flights.
        while q and count < k + 1:                                                                  #BFS while q is not empty and count is smaller than k + 1.
            newq = {}                                                                               #Initialize new queue.
            for city, cost in q.items():                                                            #Traverse city and cost in q.
                for neighbor, price in adjacentList[city]:                                          #Traverse the flights from current city.
                    new_cost = cost + price                                                         #Compute new cost.
                    if neighbor not in min_cost or min_cost[neighbor] > new_cost:                   #If neightbor is not reached or the current min cost of neighbor is greater, update the min cost of neightbor and the cost of neightbor in newq.
                        min_cost[neighbor] = new_cost
                        newq[neighbor] = new_cost
            count += 1                                                                              #Increase count.
            q = newq                                                                                #Replace q with newq.
        return -1 if dst not in min_cost else min_cost[dst]                                         #Return -1 if dst cannot be reached; otherwise return min_cost[dst],
