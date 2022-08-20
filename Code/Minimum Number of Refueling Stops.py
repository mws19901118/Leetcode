class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []                                       #Use max heap store the gas we can refuel at each station we have visited.
        stations.append([target, 0])                    #Append target to stations with 0 gas.
        stop = 0
        for p, f in stations:                           #Traverse stations.
            while startFuel < p and heap:               #While we cannot reach current station and heap is not empty, stop at the station which has most gas and refuel.
                startFuel -= heapq.heappop(heap)
                stop += 1
            if startFuel < p:                           #If still cannot reach current station, return -1.
                return -1
            heapq.heappush(heap, -f)                    #Push the gas in current station to heap.
        return stop                                     #Return the number of stops.
