class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hasIncomingEdge = [False] * n                               #Initialize a list to indicate if each vertex has incoming edge.
        for x, y in edges:                                          #Traverse edge and mark all to-vertex with incoming edge.
            hasIncomingEdge[y] = True
        return [i for i in range(n) if not hasIncomingEdge[i]]      #Return the vertexes that has no incoming edge.
