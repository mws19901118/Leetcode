class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxesLocked, keysGot = set(), set()            #Store locked boxes and keys got in 2 sets.
        q = deque(initialBoxes)                        #Initialize the deque to be initialBoxes.
        count = 0                                      #Count candy.
        while q:                                       #BFS.
            x = q.popleft()                            #Get the box at the head of deque.
            if not status[x] and x not in keysGot:     #If it is locked and we don't have key yet, add it to boxesLocked and continue.
                boxesLocked.add(x)
                continue
            count += candies[x]                        #Grab all candies in current box.
            for k in keys[x]:                          #Traverse the keys in current box.
                keysGot.add(k)                         #Add it to keysGot.
                if k in boxesLocked:                   #If the key can unlock a box, append the box to deque and remove it from boxesLocked.
                    q.append(k)
                    boxesLocked.remove(k)
            q.extend(containedBoxes[x])                #Append all boxes in current box to deque.
        return count
