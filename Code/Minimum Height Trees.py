class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbor = [[] for i in range(n)]
        degree = [0] * n
        remain = set()
        for i in range(n):                  #Store the remaining nodes.
            remain.add(i)
        for e in edges:                     #Construct the adjacency list and count degrees.
            neighbor[e[0]].append(e[1])
            neighbor[e[1]].append(e[0])
            degree[e[0]] += 1
            degree[e[1]] += 1
        q = []
        for i in range(n):                  #Find all the nodes whose degree is 1.
            if degree[i] == 1:
                q.append(i)
        while len(remain) > 2:              #BFS until no more than 2 nodes left.
            newq = []
            for start in q:                 #Store the nodes in next level.
                remain.remove(start)        #Remove current node from the remaining set.
                for end in neighbor[start]: #Update degree of nodes which connect current node.
                    degree[end] -= 1
                    if degree[end] == 1:    #If the degree is 1, append it to newq.
                        newq.append(end)
            q = newq
        return list(remain)                 #Return the list of remaining set.
