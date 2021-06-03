class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])                                                                                 #Extend the 2 boundries(0 and w) to horizontalCuts.
        verticalCuts.extend([0, w])                                                                                   #Extend the 2 boundries(0 and h) to verticalCuts.
        horizontalCuts.sort()                                                                                         #Sort horizontalCuts.
        verticalCuts.sort()                                                                                           #Sort verticalCuts.
        maxHorizontalGap = max(horizontalCuts[i + 1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1))     #Compute the max gap between 2 horizontal cuts.
        maxVerticalGap = max(verticalCuts[i + 1] - verticalCuts[i] for i in range(len(verticalCuts) - 1))             #Compute the max gap between 2 verticalC cuts.
        return maxHorizontalGap * maxVerticalGap % (10 ** 9 + 7)                                                      #The max area is maxHorizontalGap * maxVerticalGap, and return the modulo.
