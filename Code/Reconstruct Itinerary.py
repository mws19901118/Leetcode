class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)                                        #Sort tickets in lexically desending order.
        adjacentList = defaultdict(list)                                    #Build the adjacent list, and in each adjacent list the neighbors are also sorted in lexically desending order.
        for x, y in tickets:
            adjacentList[x].append(y)
        result, stack = [], ['JFK']                                         #Initialize result and stack(starting from JFK).
        while stack:                                                        #DFS.
            while adjacentList[stack[-1]]:                                  #Since there is a guaranteed result and each flight is used once and only once, just keep going at the direction of last neighbor of current city on top of stack(so its lexically smallest) until there is no more.
                stack.append(adjacentList[stack[-1]].pop())                 #Pop the neighbor from adjacent list and append it to stack.
            result.append(stack.pop())                                      #Pop the last of stack and append it to result.
        return result[::-1]                                                 #Reconstruct the routes backwards.
