class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if gas==[] or cost==[]:
            return -1
        sum=0
        total=0
        start=0
        n=len(gas)
        for i in range(n):
            sum+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if sum<0:                                   #if current sum<0, begin with the next station
                start=(i+1)%n
                sum=0
        if total>=0:
            return start
        else:
            return -1
