class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = Counter()
        for x, y in edges:                                            #Traverse edges and populate indegree of each node in DAG.
            indegree[y] += 1
        champions = [x for x in range(n) if not indegree[x]]          #Find all teams whose indegree is 0.
        return champions[0] if len(champions) == 1 else -1            #Return champions[0] if the length of champion is 1; otherwise return -1.
