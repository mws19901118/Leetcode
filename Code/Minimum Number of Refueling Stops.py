class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []                                       #Use max heap store the gas we can refuel at each station we have visited.
        stations.append([target, 0])                    #Append target to stations with 0 gas.
        stop = 0
        for s in stations:                              #Traverse stations.
            while startFuel < s[0] and heap:            #While we cannot reach current station and heap is not empty, stop at the station which has most gas and refuel.
                startFuel -= heapq.heappop(heap)
                stop += 1
            if startFuel < s[0]:                        #If still cannot reach current station, return -1.
                return -1
            heapq.heappush(heap, -s[1])                 #Push the gas in current station to heap.
        return stop                                     #Return the number of stops.
