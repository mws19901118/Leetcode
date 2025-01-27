class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        adjacentList = defaultdict(list)                                                                                                            #Build graph.
        for i, x in enumerate(favorite):                                                                                                            #Add an edge from the favorite of current person to current person.
            adjacentList[x].append(i)
        visited = set()                                                                                                                             #Store visited people.

        def tree_height(curr: int, prev: int) -> int:                                                                                               #Calculate the height of tree whose root is curr and not count the branch of prev.
            height = 0                                                                                                                              #Initialize height.
            for next in adjacentList[curr]:                                                                                                         #Traverse the neighbors of curr.
                if next != prev:                                                                                                                    #Process if next is not prev.
                    height = max(height, tree_height(next, curr))                                                                                   #Calculate the max height recursively.
            visited.add(curr)                                                                                                                       #Mark curr as visited.
            return height + 1                                                                                                                       #Return height + 1 to include curr itself.

        def cycle_length(curr: int, step: int) -> int:                                                                                              #Calculate the cycle person with current node and step.
            if curr in steps:                                                                                                                       #If current node is visited, return current step - pervious step for the same node, which yields the cycle length.
                return step - steps[curr]
            length = 0                                                                                                                              #Initialize length.
            steps[curr] = step                                                                                                                      #Set the step for current node.
            visited.add(curr)                                                                                                                       #Mark curr as visited.
            for next in adjacentList[curr]:                                                                                                         #Traverse the neighbors of curr.
                length = max(length, cycle_length(next, step + 1))                                                                                  #Calculate the cycle length recursively.
            return length                                                                                                                           #Return length.

        jointTreeLength = sum(tree_height(i, x) + tree_height(x, i) for i, x in enumerate(favorite) if i not in visited and favorite[x] == i)       #Find all 2-nodes cycles(2 people whose favorite person is each other), then sum up all the joint tree length(sum of tree heights of 2 trees whose roots are the 2 nodes in cycle). 
        maxCycleLength = 0                                                                                                                          #Initialize max cycle length.
        for i, x in enumerate(favorite):                                                                                                            #Traverse favorite.
            if i in visited:                                                                                                                        #If i is visited, skip.
                continue
            steps = defaultdict(int)                                                                                                                #Initialize steps for each node before finding cycle length.
            maxCycleLength = max(maxCycleLength, cycle_length(i, 0))                                                                                #Find the current cycle length and update max cycle length if necessary.
        return max(jointTreeLength, maxCycleLength)                                                                                                 #To seat the most empployees, it is the max between longest cycle and total joint tree lengths.
