class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)                                                                #Record the number of houses.
        if m == 0:
            return 0
        n = len(costs[0])                                                             #Record the number of colors.
        if n == 0:
            return 0
        minIndex = -1                                                                 #Record the index of last used color.
        firstMin = 0x7fffffff                                                         #Record the min sum of costs before current house.
        secondMin = 0x7fffffff                                                        #Record the second min sum of costs before current house.
        for j in range(n):                                                            #Find minIndex and firstMin for the first house.
            if costs[0][j] < firstMin:
                firstMin = costs[0][j]
                minIndex = j
        for j in range(n):                                                            #Find secondMin for the first house.
            if j == minIndex:                                                         #When comes to the firstMin, ignore it.
                continue
            if costs[0][j] < secondMin:
                secondMin = costs[0][j]
        for i in range(1, m):
            localMinIndex = -1                                                        #Record the index of min cost color except for the color used by last house.
            localFirstMin = 0x7fffffff                                                #Record the min cost except for the color used by last house.
            localSecondMin = 0x7fffffff                                               #Record the second min cost except for the color used by last house.
            for j in range(n):                                                        #Find localMinIndex and localFirstMin for the current house.
                if j == minIndex:                                                     #When comes to the last used color, ignore it.
                    continue
                if costs[i][j] < localFirstMin:
                    localFirstMin = costs[i][j]
                    localMinIndex = j
            for j in range(n):                                                        #Find localFirstMin for the current house.
                if j == minIndex or j == localMinIndex:                               #When comes to the last used coloe or localMinIndex, ignore it.
                    continue
                if costs[i][j] < localSecondMin:
                    localSecondMin = costs[i][j]
            temp = secondMin + costs[i][minIndex]                                     #Recoed the min cost if don't use the last used color on last house but use it on current house.
            if temp < firstMin + localFirstMin:                                       #If temp is smaller than the min cost do not using last used color on current house, using last used color on current house is a better solution.
                secondMin = firstMin + localFirstMin                                  #Update secondMin.
                firstMin = temp                                                       #Update firstMin
            else:                                                                     #Otherwise, using the min cost color except for the color used by last house is a better solution.
                if temp < firstMin + localSecondMin:                                  #Determin which value is the new secondMin and update it.
                    secondMin = temp
                else:
                    secondMin = firstMin + localSecondMin
                firstMin += localFirstMin                                             #Update firstMin.
                minIndex = localMinIndex                                              #Update minIndex.
        return firstMin                                                               #Return firstMin.
