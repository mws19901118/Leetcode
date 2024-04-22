class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndsSet = set(deadends)                                                   #Convert dean ends list to set.
        q = ["0000"]                                                                  #Initialize queue with "0000".
        visited = set(q)                                                              #Use a set to store all visited state.
        result = 0
        while q:                                                                      #BFS while q is not empty.
            newq = []                                                                 #Initialize a new queue.
            for s in q:                                                               #Traverse all states in q.
                if s in deadEndsSet:                                                  #If is dead end, skip current state.
                    continue
                if s == target:                                                       #If reaches target, return turns directly.
                    return result
                for i, turn in product(range(4), [-1, 1]):                            #Try all 4 wheels and 2 directions.
                    afterTurn = s[:i] + str((int(s[i]) + turn) % 10) + s[i + 1:]      #Get the state after turn.
                    if afterTurn not in visited:                                      #If it is not visited, add it to visited and newq.
                        visited.add(afterTurn)
                        newq.append(afterTurn)
            q = newq                                                                  #Replace q with newq.
            result += 1
        return -1                                                                     #Return -1 if cannot reach target.
