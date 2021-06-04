class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndsSet = set(deadends)                                                   #Convert dean ends list to set.
        q = set(["0000"])                                                             #Initialize queue with "0000".
        visited = set()                                                               #Use a set to store all visited state.
        turns = 0                                                                     #Initialize number of turns.
        while q:                                                                      #NFS while q is not empty.
            newq = set()                                                              #Initialize a new queue.
            for x in q:                                                               #Traverse all states in q.
                if x == target:                                                       #If reaches target, return turns directly.
                    return turns
                if x in deadEndsSet:                                                  #If is dead end, skip current state.
                    continue
                for i in range(4):                                                    #Try all 4 wheels.
                    plusOne = x[:i] + str((int(x[i]) + 1) % 10) + x[i + 1:]           #Turn forward, and add the state to newq if it's not visited.
                    if plusOne not in visited:
                        newq.add(plusOne)
                    minusOne = x[:i] + str((int(x[i]) - 1) % 10) + x[i + 1:]          #Turn backward, and add the state to newq if it's not visited.
                    if minusOne not in visited:
                        newq.add(minusOne)
            visited |= q                                                              #Update visited.
            q = newq                                                                  #Replace q with newq.
            turns += 1                                                                #Increase turns.
        return -1                                                                     #Return -1 if cannot reach target.
