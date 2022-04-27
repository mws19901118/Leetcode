class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adjacentList = [[] for _ in range(len(s))]                              #Build a undirected graph for pairs.
        for x, y in pairs:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
            
        result = [None] * len(s)                                                #Store the characters after swaps.
        index = 0                                                               #Store the index of first remaining unvisited character.
        while index < len(result):                                              #Iterate each component of graph.
            q = [index]                                                         #BFS the current component.
            visited = set([index])                                              #Store indexes of component.
            characters = []                                                     #Store characters of component.
            while q:
                newq = []
                for x in q:
                    characters.append(s[x])
                    for y in adjacentList[x]:
                        if y not in visited:
                            visited.add(y)
                            newq.append(y)
                q = newq
                
            for i, x in zip(sorted(list(visited)), sorted(characters)):         #Assign sorted characters on sorted indexes respectively.
                result[i] = x
                
            while index < len(result) and result[index] is not None:            #Go to next component.
                index += 1
                
        return "".join(result)                                                  #Join result and return.
