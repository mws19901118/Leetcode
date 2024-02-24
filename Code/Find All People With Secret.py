class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.append([0, firstPerson, 0])                                              #Add a virtual meeting between person 0 and first person at time 0.
        adjacentList = defaultdict(list)                                                  #Initialize adjacent list.
        for x, y, t in meetings:                                                          #Traverse meetings.
            adjacentList[x].append((t, y))                                                #Add (t, y) to adjacentList[x].
            adjacentList[y].append((t, x))                                                #Add (t, x) to adjacentList[x].
        for x in adjacentList:                                                            #Sort each adjacent list.
            adjacentList[x].sort()
        earliestTime = [inf] * n                                                          #Store the earlist time of a person knows the secret.
        earliestTime[0] = 0                                                               #Initially, person 0 knows the secret.
        q = {0: 0}                                                                        #Also initialize the queue to be person 0 knows secret at time 0.
        known = set()                                                                     #Store people known secret.
        while q:                                                                          #BFS.
            newq = {}                                                                     #Initialize new queuq.
            for x, currentTime in q.items():                                              #Traverse current person and time in q.
                while adjacentList[x] and adjacentList[x][-1][0] >= currentTime:          #While the adjacent list of current person is not empty and the last meeting time is after current time, pop the adjacent list.
                    t, y = adjacentList[x].pop()
                    if t < earliestTime[y]:                                               #If the meeting time is smaller than the earlist time person y knows the secret, update earliestTime[y] and add or update newq[y] to t.
                        earliestTime[y] = t
                        newq[y] = t
            known |= q.keys()                                                             #Add all people in q to known.
            q = newq                                                                      #Replace q with newq.
        return list(known)                                                                #Return the list of known.
