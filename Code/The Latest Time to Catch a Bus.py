class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()                                                                          #Sort buses departure time.
        passengers.sort()                                                                     #Sort passengers arrival time.
        result = -1                                                                           #Initialize result to be -1.
        j = 0                                                                                 #Initialize the pointer to traverse passengers.
        for i, x in enumerate(buses):                                                         #Traverse buses.
            count = 0                                                                         #Count the passengers for current bus.
            while j < len(passengers) and passengers[j] <= x and count < capacity:            #Move forward j while the passengers arrive before x and there are still room on bus.
                if j == 0 or passengers[j - 1] != passengers[j] - 1:                          #Since passengers[j] can take current bus, if passengers[j] - 1 is not taken by other passengers, if arriving at that time, it is guarenteed to catch current bus. 
                    result = max(result, passengers[j] - 1)                                   #So update result if necessary.
                j += 1                                                                        #Move forward j.
                count += 1                                                                    #Increase count.
            if count < capacity and x != passengers[j - 1]:                                   #If bus is not full and the departure time of current bus is not taken by any passenger, arriving at current time is guarenteed to catch current bus. 
                result = max(result, x)                                                       #So update result if necessary.
        return result                                                                         #Return result.
