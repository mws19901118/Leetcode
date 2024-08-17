class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0].copy()                                                      #Store the max point ending at each row, initially it is the first row. 
        for row in points[1:]:                                                     #Traverse other rows.
            leftMax = dp.copy()                                                    #Initialize the max influence from left to be dp.
            for i in range(1, len(dp)):                                            #Traverse leftMax.
                leftMax[i] = max(leftMax[i], leftMax[i - 1] - 1)                   #Update leftMax[i] if leftMax[i - 1] - 1 is larger.
            rightMax = dp.copy()                                                   #Initialize the max influence from right to be dp.
            for i in reversed(range(len(dp) - 1)):                                 #Traverse rightMax backwards.
                rightMax[i] = max(rightMax[i], rightMax[i + 1] - 1)                #Update rightMax[i] if rightMax[i + 1] - 1 is larger.
            dp = [x + max(leftMax[i], rightMax[i]) for i, x in enumerate(row)]     #Update dp for current row; for each column i, the max point is current point plus the max of leftMax[i] and rightMax[i].
        return max(dp)                                                             #Return max of dp.
