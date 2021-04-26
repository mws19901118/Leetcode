class Solution:
    def dfs(self, egdes: dict, discovery: List[int], low: List[int], time: int, result: List[List[int]], curr: int, prev: int):      #Tarjan's algorithm.
        discovery[curr] = low[curr] = time
        time += 1
        for x in egdes[curr]:
            if not discovery[x]:
                self.dfs(egdes, discovery, low, time, result, x, curr)
                low[curr] = min(low[curr], low[x])
            elif x != prev:
                low[curr] = min(low[curr], discovery[x])
            if low[x] > discovery[curr]:
                result.append([curr, x])
                
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        egdes = defaultdict(list)
        for a, b in connections:
            egdes[a].append(b)
            egdes[b].append(a)
        discovery, low, result = [0] * n, [0] * n, []
        self.dfs(egdes, discovery, low, 1, result, 0, -1)
        return result
