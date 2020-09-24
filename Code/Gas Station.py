class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currentSum, total, start, n = 0, 0, 0, len(gas)
        for i in range(n):                      #Iterate through all stations.
            currentSum += gas[i]-cost[i]        #Calculate the remaining gas from current start station to this station.
            total += gas[i]-cost[i]             #Calculate the total gas.
            if currentSum < 0:                  #If the remaining gas from current start station to this station is smaller than 0, it means cannot finish the trip from current start station.
                start = (i + 1) % n             #Start from next station.
                currentSum = 0                  #Reset the remaining gass.
        return start if total >= 0 else -1      #If total gas is not smaller than 0, the trip can be finished, returning start station; otherwise, trip cannot be finished, return -1.
