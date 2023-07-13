class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   #Use BFS topological sort.
        graph = defaultdict(list)
        indegree = [0 for x in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])                                                #If a is a prerequisite of b, generate an edge pointing to b from a.
            indegree[p[1]] += 1                                                     #Calculate the in-degree.
        q = [i for i in range(numCourses) if not indegree[i]]                       #Find all classes with no prerequisite.
        count = 0                                                                   #Count classes that have finished all prerequisites.
        while q:                                                                    #BFS.
            newq = []
            for x in q:                                                             #For each class in queue, update the in-degree of its neighbors after traverse.
                for y in adjacentList[x]:
                    indegree[y] -= 1
                    if not indegree[y]:                                             #If neighbor has 0 in-degree, all prerequisites are finished, add it to newq.
                        newq.append(y)
            count += len(q)                                                         #Add len(q) to count.
            q = newq                                                                #Replace q with newq.
        return count == numCourses                                                  #Return if all classes have finished all prerequisites.
