class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank = Counter()                                                                                            #Count the indegree of each city.
        roadsSet = set()
        for x, y in roads:                                                                                          #Traverse roads
            rank[x] += 1                                                                                            #Increase the indegree of 2 cities of current road.
            rank[y] += 1
            roadsSet.add((x, y))                                                                                    #Store the city pair in set.
        result = 0
        for i in range(n):                                                                                          #Traverse each pairs of cities.
            for j in range(i):
                result = max(result, rank[i] + rank[j] - int((i, j) in roadsSet or (j, i) in roadsSet))             #Sum up ranks of 2 cities and minues one if there is a road directly connecting 2 cities, then update result if necessary.
        return result
