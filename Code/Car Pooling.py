class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for trip in trips:                            #Split a trip into 2 events, picking up and dropping off.
            events.append((trip[1], trip[0]))         #Picking up event with location and capacity change.
            events.append((trip[2], -trip[0]))        #Dropping off event with location and capacity change.
        events.sort()                                 #Sort events by location in asending order, so if there are both picking up and dropping off in same location, dropping off comes first.
        for event in events:                          #For each event, extract number of passengers from capacity.
            capacity -= event[1]
            if capacity < 0:                          #If capacity is negative, return false.
                return False
        return True                                   #If not, return true.
