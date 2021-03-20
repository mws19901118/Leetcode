class UndergroundSystem:

    def __init__(self):
        self.customerDict = defaultdict(tuple)                                                                                          #Use a dict to store the check in time and station for a given customer id.
        self.travelDict = defaultdict(lambda:(0, 0))                                                                                    #Use a dict to store the current total travel time and travel count between 2 stations.

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerDict[id] = (t, stationName)                                                                                        #Customer check in, add the current time and station name to customer dict.

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStationName = self.customerDict[id][1]                                                                                     #Customer check out, find the customer check in station first.
        currentStats = self.travelDict[(startStationName, stationName)]                                                                 #Find the current total travel time and travel count between the check in station and check out station.
        self.travelDict[(startStationName, stationName)] = (currentStats[0] + t - self.customerDict[id][0], currentStats[1] + 1)        #Update total travel time and travel count.
        del self.customerDict[id]                                                                                                       #Delete customer from customer dict.
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        currentStats = self.travelDict[(startStation, endStation)]                                                                      #Calculate average time from total travel time and travel count.
        return currentStats[0] * 1.0 / currentStats[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
