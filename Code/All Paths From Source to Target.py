class Solution:
    def DFS(self, graph: List[List[int]], stack: List[int], result: List[List[int]]):
        if stack and stack[-1] == len(graph) - 1:                                           #If the last element in stack is target, append the deep copy of stack to result and return.
            result.append(copy.deepcopy(stack))
            return
        for x in graph[stack[-1]]:                                                          #Traverse the neighbors of stack[-1] and keep DFS.
            stack.append(x)
            self.DFS(graph, stack, result)
            stack.pop()
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.DFS(graph, [0], result)                                                        #DFS.
        return result
