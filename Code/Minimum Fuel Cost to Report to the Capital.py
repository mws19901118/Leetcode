class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacentList = collections.defaultdict(list)                                  #Build the adjacent list.
        for x, y in roads:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        
        def DFS(curr: int, prev: int) -> (int, int):                                  #DFS.
            people, gas = 1, 0                                                        #Intitialize the total people and gas needed for all nodes under current substree. 
            for x in adjacentList[curr]:                                              #Traverse the adjacent list of current node.
                if x == prev:                                                         #If x is prev, skip.
                    continue
                people_from_next_node, gas_from_next_node = DFS(x, curr)              #Keep DFS in x.
                people += people_from_next_node                                       #Add people from x to people.
                gas += gas_from_next_node                                             #Add gas from x to all gas.
            if curr != 0:                                                             #If curr is not capital, add gas for ceil(people / seats) to sit all people, 
                gas += ceil(people / seats)
            return people, gas                                                        #Return people and gas.

        return DFS(0, None)[1]                                                        #Start DFS from 0 and return total gas.
