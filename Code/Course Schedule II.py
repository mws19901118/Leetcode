class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):             #Use the same topological sort used in Course Schedule I.
        if prerequisites==[]:
            return [i for i in range(numCourses)]
        graph=[[] for i in range(numCourses)]
        indgree=[0 for i in range(numCourses)]
        order=[]                                                #Record the order of courses.
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indgree[i[0]]+=1
            
        stack=[]
        for i in range(numCourses):
            if indgree[i]==0:
                stack.append(i)
                
        while stack!=[]:
            node=stack.pop()
            order.append(node)                                  #If all the prerequisites of current course are taken, append current course to order.
            while graph[node]!=[]:
                temp=graph[node].pop()
                indgree[temp]-=1
                if indgree[temp]==0:
                    stack.append(temp)
                    
        if len(order)<numCourses:                               #If the length of order of courses is less than the number of courses, there is a cycle in the direct graph. Thus, return false. 
            return []
        else:
            return order
