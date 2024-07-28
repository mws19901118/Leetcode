class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adjacentList = defaultdict(list)                                  #Build adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)
        time1, time2 = [-1] * (n + 1), [-1] * (n + 1)                     #Store the 1st and 2nd time of visiting each node.
        q = deque([(1, 1)])                                               #Initialize deque with (1, 1), meaning starting from node 1 so it is already visited once.
        while q:                                                          #BFS,
            x, visitCount = q.popleft()                                   #Pop the left of deque.
            t = time1[x] if visitCount == 1 else time2[x]                 #Get the time of arriving current node by the visit count.
            if (t // change) & 1:                                         #If it is red light, wait until next green light.
                t = ((t // change) + 1) * change
            arrivingTime = t + time                                       #Add time to t to be the arriving time to neighbor.
            for y in adjacentList[x]:                                     #Traverse each neighbor.
                if time1[y] == -1:                                        #If neighbor is not visited, update its 1st visited time and append (y, 1) to deque.
                    time1[y] = arrivingTime
                    q.append((y, 1))
                elif time2[y] == -1 and time1[y] != arrivingTime:         #Otherwise if neighbor is not visited 2nd time and the arriving time is not same as 1st time, update its 2nd visited time and append (y, 2) to deque.
                    time2[y] = arrivingTime
                    q.append((y, 2))
                    if y == n:                                            #If y is n, return arriving time.
                        return arrivingTime
