class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(numCourses)]                                                       #Record the count of unfufilled prerequisites of each course.
        edges = [[] for i in range(numCourses)]                                                         #Record the courses that current course is their prerequisite.
        for p in prerequisites:                                                                         #Build graph.
            inDegree[p[0]] += 1
            edges[p[1]].append(p[0])
        stack = [i for i in range(numCourses) if inDegree[i] == 0]                                      #Inialize stack with the courses which have no prerequisite.
        order = []                                                                                      #Store the course order.
        while stack:                                                                                    #DFS.
            x = stack.pop()                                                                             #Take the last course in stack and add it to order.
            order.append(x)
            for y in edges[x]:                                                                          #Update the unfufilled prerequisites.
                inDegree[y] -= 1                                                                        #If no unfufilled prerequisites, add course to stack.
                if inDegree[y] == 0:
                    stack.append(y)
        return [] if len(order) < numCourses else order                                                 #If the length of order is smaller than number of courses, there are cycles, so return empty list. Otherwise return order directly.
