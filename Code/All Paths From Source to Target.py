import copy
class Solution:
    def DFS(self, graph: List[List[int]], stack: List[int], result: List[List[int]]):       #Simple DFS
        if stack and stack[-1] == len(graph) - 1:
            result.append(copy.deepcopy(stack))
            return
        for x in graph[stack[-1]]:
            stack.append(x)
            self.DFS(graph, stack, result)
            stack.pop()
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.DFS(graph, [0], result)
        return result
