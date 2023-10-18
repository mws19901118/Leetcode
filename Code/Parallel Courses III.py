class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        inDegree, adjacentList = defaultdict(int), defaultdict(list)    #Build graph.
        for x, y in relations:
            inDegree[y] += 1
            adjacentList[x].append(y)
        q = [i for i in range(1, n + 1) if not inDegree[i]]             #Find all the courses without prerequisite.
        months = defaultdict(int)                                       #Store the months to finish each course.
        while q:                                                        #BFS.
            newq = []
            for x in q:                                                 #Traverse all courses in queue.
                months[x] += time[x - 1]                                #Finish current course.
                for y in adjacentList[x]:                               #Traverse all neighbors of x.
                    months[y] = max(months[y], months[x])               #Update months[y], which now is the time needed to finish all prerequisites, if necessary.
                    inDegree[y] -= 1                                    #Reduce indegree of y because one prerequisite is finished.
                    if not inDegree[y]:                                 #If all prerequisites are finished, append y to newq.
                        newq.append(y)
            q = newq                                                    #Replace q with newq.
        return max(months.values())                                     #Return the max of months.
