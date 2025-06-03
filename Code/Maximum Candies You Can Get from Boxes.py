class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q, locked = deque([x for x in initialBoxes if status[x]]), set([x for x in initialBoxes if not status[x]])            #For each initial boxes, if it is open, put it in a deque; otherwise, put it in a set of locked boxes.
        result = 0
        while q:                                                                                                              #BFS.
            x = q.popleft()                                                                                                   #Popleft q to get current box.
            result += candies[x]                                                                                              #Take all the candies inside.
            for y in keys[x]:                                                                                                 #Traverse the keys inside.
                status[y] = 1                                                                                                 #Mark the corresponding box as open.
                if y in locked:                                                                                               #If the box is previously locked, now it can be opened, so append it to q and remove it from locked.
                    q.append(y)
                    locked.remove(y)
            for y in containedBoxes[x]:                                                                                       #Traverse the boxes inside.
                if not status[y]:                                                                                             #If it is closed, add it to locked.
                    locked.add(y)
                else:                                                                                                         #Otherwise, append it to q.
                    q.append(y)
        return result
