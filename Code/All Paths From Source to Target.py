    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set([])
        result = []
        def DFS(stack: List[int]):
            if stack[-1] == len(graph) - 1:                                             #If the last element in stack is target, append the deep copy of stack to result and return.
                result.append(copy.deepcopy(stack))
                return
            for x in graph[stack[-1]]:                                                  #Traverse the neighbors of stack[-1] and keep DFS.
                stack.append(x)
                visited.add(x)
                DFS(stack)
                visited.remove(x)
                stack.pop()
        DFS([0])                                                                        #DFS.
        return result
