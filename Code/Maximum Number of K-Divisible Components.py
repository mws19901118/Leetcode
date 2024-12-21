class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjacentList = defaultdict(set)                                  #Initialize adjacent list.
        for x, y in edges:                                               #Traverse edges to populate adjacent list.
            adjacentList[x].add(y)
            adjacentList[y].add(x)
        result = 0                                                       #Initialize result.
        def dfs(curr: int, prev: int) -> None:                           #DFS.
            nonlocal result                                              #Reference result inside DFS.
            children = [x for x in adjacentList[curr] if x != prev]      #Get all children of curr.
            for x in children:                                           #Keep DFS at each child.
                dfs(x, curr)
            if not values[curr] % k:                                     #If current value is divisible by k, increase result.
                result += 1
            else:                                                        #Otherwise merge the value with prev.
                values[prev] += values[curr]
            adjacentList[prev].discard(curr)                             #Remove curr from the adjacent list of orev.
        dfs(0, None)                                                     #DFS from node 0.
        return result
