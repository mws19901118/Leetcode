class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        outnodes = [[] for i in range(n)]           #Record the possible next node of each node.
        for e in edges:                             #Because it's undirected graph, append out nodes for each node in an edge.
            outnodes[e[0]].append(e[1])
            outnodes[e[1]].append(e[0]).
        queue = outnodes[0]                         #Start BFS at out nodes of node 0.
        oldq = set([0])                             #Record the nodes arrived in last level(initially node 0).
        arrived = set([0])                          #Use a set to record arrived nodes.
        while queue != []:                          #BFS while current level is not empty.
            newq = []                               #Record the nodes in next level.
            for node in queue:
                if node in arrived:                 #If current node is arrived before, return false,  because there are cycles.
                    return False
                arrived.add(node)                   #Otherwise add current node to arrived nodes.
                for next in outnodes[node]:
                    if next not in oldq:            #For every out nodes of current nodes, if it is not in last level(because edge is undirected), append it to next level.
                        newq.append(next)
            oldq = set(queue)                       #Update last level using current level.
            queue = newq                            #Update current level using next level.
        if len(arrived) < n:                        #If the number of arrived nodes is smaller than n, the graph is not connected, thus it is not tree, return false.
            return False
        else:                                       #Otherwise the graph is undirected connected acyclic graph, which is tree, return true.
            return True
