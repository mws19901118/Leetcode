from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   #Use BFS topological sort.
        graph = defaultdict(list)
        indegree = [0 for x in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])                                                #If a is a prerequisite of b, generate an edge pointing to b from a.
            indegree[p[1]] += 1                                                     #Calculate the in-degree.
        q = [x for x in range(numCourses) if indegree[x] == 0]                      #Find all classes with no prerequisite.
        while q:                                                                    #BFS.
            nextq = []
            for x in q:
                for y in graph[x]:
                    indegree[y] -= 1                                                #For each class in BFS, update the in-degree of its neighbors after traverse.
                    if indegree[y] == 0:                                            #If neighbor has 0 in-degree, all prerequisites are finished, add it to q.
                        nextq.append(y)
            q = nextq
        return all(indegree[x] == 0 for x in range(numCourses))                     #Return if all classes have finished all prerequisites.
