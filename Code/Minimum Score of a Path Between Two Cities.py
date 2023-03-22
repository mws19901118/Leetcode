class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjacentList = defaultdict(list)                    #Build adjacent list, with distance.
        for a, b, d in roads:
            adjacentList[a].append((b, d))
            adjacentList[b].append((a, d))
        scores = [float('inf')] * (n + 1)                   #Initialize score for each city to be infinite.
        q = [1]
        while q:                                            #BFS.
            newq = []
            for x in q:
                for y, d in adjacentList[x]:
                    if min(scores[x], d) < scores[y]:       #If the scores[y] will be smaller when visiting from x, append y to newq and update scores[y].
                        newq.append(y)
                        scores[y] = min(scores[x], d)
            q = newq
        return scores[n]                                    #Return scores[y].
