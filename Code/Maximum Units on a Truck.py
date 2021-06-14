class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])              #Sort boxes by number of units in box in descending order.
        i, units = 0, 0
        while truckSize > 0 and i < len(boxTypes):        #Traverse boxes while truck is not full and there are boxes remain.
            count = min(boxTypes[i][0], truckSize)        #Count of current box to add is the smaller of number of current box and remain truck size.
            units += count * boxTypes[i][1]               #Add units.
            truckSize -= count                            #Update remain truck size.
            i += 1
        return units
