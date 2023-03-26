class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)                                  #Store if each node is visited.
        steps = [len(edges) + 1] * len(edges)                           #Store the steps from traverse beginning for each node. Since each node will only be visited once, the relative steps won't have conflict. 

        def DFS(x: int, step: int):                                     #DFS.
            if visited[x] or edges[x] == -1:                            #If x is visited or it has no outgoing edge, return -1 because current travrese is either not needed or ended.
                return -1

            if steps[x] < len(edges) + 1:                               #If steps[x] is not its initial value, it is visted before so there is a cycle whose size is current step minus steps[x].
                return step - steps[x]

            steps[x] = step                                             #Update steps[x].
            result = DFS(edges[x], step + 1)                            #Keep DFS and get result.
            visited[x] = True                                           #Mark current node as visited.
            return result                                               #Return result.

        return max(DFS(i, 0) for i in range(len(edges)))                #DFS from each node and return the max result.
