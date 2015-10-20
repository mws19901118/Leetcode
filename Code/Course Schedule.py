class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):               #The problem equals judging if there is a circle in a directed graph. Here I use topological sorting.
        if prerequisites==[]:                                     #If there is no prerequisites, return true.
            return True
        graph=[[] for i in range(numCourses)]                     #Record the list of end points of each node.
        indgree=[0 for i in range(numCourses)]                    #Record in-degree of each node.
        visited=[False for i in range(numCourses)]                #Record if this node is visited.
        for i in prerequisites:
            graph[i[1]].append(i[0])                              #If a is a prerequisite of b, generate an edge pointing to b from a.
            indgree[i[0]]+=1                                      #Calculate the in-degree.
            
        stack=[]
        for i in range(numCourses):
            if indgree[i]==0:
                stack.append(i)                                   #Push the nodes with 0 in-degree to the stack.
                
        while stack!=[]:                                          #Loop until the stack is empty.
            node=stack.pop()                                      #Pop the top of stack.
            visited[node]=True                                    #Set its status as visited.
            while graph[node]!=[]:
                temp=graph[node].pop()                            #Delete each edge starting at it.
                indgree[temp]-=1                                  #Update the in-degree of each ending point.
                if indgree[temp]==0:                              #if the in-degree of ending point is 0, push the ending point to the stack.
                    stack.append(temp)
                    
        for i in range(numCourses):
            if visited[i]==False:                                 #If there is still node unvisited, there is a circle in the graph, thus return false.
                return False
        return True
