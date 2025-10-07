class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [1] * len(rains)                #Initialize result.
        dry = SortedList()                       #Store the days available for drying.
        last = {}                                #Store the last a lake is filled by rain.
        for i, x in enumerate(rains):            #Traverse rains.
            if not x:                            #If current day is not rainy, add the day to dry.
                dry.add(i)
            else:                                #Otherwise, find a lake to dry if there will be flood.
                result[i] = -1                   #Update current day in result.
                if x in last:                    #If the lake is already filled, find the 
                    index = dry.bisect(last[x])  #Find the first possible day to dry the lake after it was filled last time.
                    if index == len(dry):        #If no such day, then it is impossible to avoid flood, so return empty list.
                        return []
                    result[dry[index]] = x       #Dry current lake at that day.
                    dry.discard(dry[index])      #Remove the day from days available for drying.
                last[x] = i                      #Reset the last day current lake is filled to current day.
        return result
