class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjacentList, inDegree = [[] for _ in range(n + 1)], [0] * (n + 1)                  #Initialize adjacent list and indegree of each course.
        for x, y in relations:                                                              #Build adjacent list and indegree.
            adjacentList[x].append(y)
            inDegree[y] += 1
        q = [i for i in range(1, n + 1) if inDegree[i] == 0]                                #Start BFS from the courses with no prerequisite.
        count = 0                                                                           #Count semester.
        while q and n:                                                                      #BFS while queue is not empty and not all courses have been taken.
            newq = []                                                                       #Initialize new queue.
            for x in q:                                                                     #Traverse queue.
                for y in adjacentList[x]:                                                   #Take course x in this semester so all neighbors in its adjacent list will have one less prerequisite.
                    inDegree[y] -= 1
                    if not inDegree[y]:                                                     #If y has no more prerequisite, append it to newq to be taken in next semester.
                        newq.append(y)
            n -= len(q)                                                                     #Substract the course taken this semester from n.
            q = newq                                                                        #Replace queue with new queue.
            count += 1                                                                      #Move to next semester.
        return -1 if n else count                                                           #If there are still course not taken, return -1; otherwise, return count.
