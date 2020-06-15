from collections import defaultdict
class Solution:
    def DFS(self, src, dst, stops, graph, cache, trace):
        if stops < 0:                                                           #If k is smaller than 0, means there is no way to fly from start to destination, return -1.
            return -1
        if src == dst:                                                          #If start and destination are same, return 0 since no fly is needed.
            return 0
        minPrice = 0x7fffffff                                                   #Initialize minPrice with max value.
        trace.add(src)                                                          #Add start to trace.
        if (src, dst, stops) in cache:                                          #If the tuple of start, destination and stops is in cache, set minPrice to be cached value.
            minPrice = cache[(src, dst, stops)]
        else:
            for stop in graph[src]:                                             #Otherwise, for each city can be reached from start and hasn't been reached, do BFS with stop equals to k - 1 to calculate the minPrice from intermediate stop to destination.
                if stop not in trace:
                    temp = self.DFS(stop, dst, stops - 1, graph, cache, trace)
                    if temp != -1:                                              #If can reach destination from intermediate stop, plus the result from last step with the price from start to intermediate stop to calculate the minPrice from start to destination through intermediate stop.
                        minPrice = min(minPrice, temp + graph[src][stop])
            if minPrice == 0x7fffffff:                                          #If minPrice is still max value, it means cannot find a way from start to destination.
                minPrice = -1
            cache[(src, dst, stops)] = minPrice                                 #Add result to cache for the tuple of the tuple of start, destination and stops
        trace.remove(src)                                                       #Remove start from trace.
        return minPrice                                                         #Return minPrice.
            
    def findCheapestPrice(self, n: 'int', flights: 'List[List[int]]', src: 'int', dst: 'int', K: 'int') -> 'int':
        graph = defaultdict(dict)                                               #Use a dict of dict to represent the graph.
        for e in flights:                                                       #For each flight, create an edge from start to destination with value to be price.
            graph[e[0]][e[1]] = e[2]
        cache = {}                                                              #Cache the result by a tuple of start, destination and stops.
        trace = set()                                                           #Store the trace of BFS.
        return self.DFS(src, dst, K + 1, graph, cache, trace)                   #BFS.
