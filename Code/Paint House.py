class Solution(object):
    def minCost(self, costs):                   #Ths same as Paint House II
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)
        if m == 0:
            return 0
        n = len(costs[0])
        if n == 0:
            return 0
        minIndex = -1
        firstMin = 0x7fffffff
        secondMin = 0x7fffffff
        for j in range(n):
            if costs[0][j] < firstMin:
                firstMin = costs[0][j]
                minIndex = j
        for j in range(n):
            if j == minIndex:
                continue
            if costs[0][j] < secondMin:
                secondMin = costs[0][j]
        for i in range(1, m):
            localMinIndex = -1
            localFirstMin = 0x7fffffff
            localSecondMin = 0x7fffffff
            for j in range(n):
                if j == minIndex:
                    continue
                if costs[i][j] < localFirstMin:
                    localFirstMin = costs[i][j]
                    localMinIndex = j
            for j in range(n):
                if j == minIndex or j == localMinIndex:
                    continue
                if costs[i][j] < localSecondMin:
                    localSecondMin = costs[i][j]
            temp = secondMin + costs[i][minIndex]
            if temp < firstMin + localFirstMin:
                secondMin = firstMin + localFirstMin
                firstMin = temp
            else:
                if temp < firstMin + localSecondMin:
                    secondMin = temp
                else:
                    secondMin = firstMin + localSecondMin
                firstMin += localFirstMin
                minIndex = localMinIndex
        return firstMin
