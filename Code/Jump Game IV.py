class Solution:
    def minJumps(self, arr: List[int]) -> int:
        newArr = []                                       #Preprocess. For a number that appears at least 2 consecutive times in arr, we only need 2 of them.
        i = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
            newArr.append(arr[i])
            if j - i >= 2:
                newArr.append(arr[i])
            i = j
        
        indexes = defaultdict(list)                       #Store the indexes of each number
        for i, x in enumerate(newArr):
            indexes[x].append(i)
        graph = defaultdict(set)                          #Build graph, node is index and there is an edge between 2 nodes if we can jump from one to the other.
        for i, x in enumerate(newArr):
            if i > 0:
                graph[i].add(i - 1)
            if i < len(newArr) - 1:
                graph[i].add(i + 1)
            for j in indexes[x]:
                if j != i:
                    graph[i].add(j)
        
        steps = 0
        q = set([0])
        visited = set()
        while q:                                          #BFS and count steps.
            newq = set()
            for x in q:
                if x == len(newArr) - 1:                  #Return steps when we reach the end.
                    return steps
                for y in graph[x]:
                    if y not in q and y not in visited:
                        newq.add(y)
                visited.add(x)
            steps += 1
            q = newq
