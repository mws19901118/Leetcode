class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        choices = ['A', 'C', 'G', 'T']                                #List valid choices.
        if start not in bank:                                         #If start not in bank, add it to bank.
            bank.append(start)
        indexes = {x: i for i,x in enumerate(bank)}                   #Build the gene to index map.
        adjacentList = defaultdict(list)                              #Build the adjacent list.
        for i, x in enumerate(bank):                                  #Traverse bank.
            for j in range(len(x)):                                   #Enumerate each position of x.
                for y in choices:                                     #Try each choice.   
                    if y == x[j]:                                     #Mutation can not be same as current choice.
                        continue
                    mutant = x[:j] + y + x[j + 1:]                    #Generate mutant.
                    if mutant in indexes:                             #If mutant in bank, add the index of mutant in adjacent list of x.
                        adjacentList[i].append(indexes[mutant])
        step = 0                                                      #Initialize step.
        q, visited = set([indexes[start]]), set()
        while q:                                                      #BFS.
            visited |= q
            newq = set()
            for x in q:
                if bank[x] == end:                                    #Return step if reaches end.
                    return step
                for y in adjacentList[x]:
                    if y in visited:
                        continue
                    newq.add(y)
            q = newq
            step += 1
        return -1                                                     #Return -1 if not.
                
