class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)                               #Sort satisfaction in descending order.
        coefficient, cumulativeSum = 0, 0                               #Initialize the coefficient and cumulativeSum to be both 0.
        for s in satisfaction:                                          #Traverse satisfaction.
            cumulativeSum += s                                          #Update cumulative sum.
            if cumulativeSum <= 0:                                      #If it is smaller than or equal to 0, it no longer worth adding it to coefficient, so stop loop.
                break
            coefficient += cumulativeSum                                #Add cumulativeSum to coefficient so higer satisfaction a dish gets more multiply in coefficient.
        return coefficient                                              #Return coefficient.
