class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache                                                                                    #Cache result of dp.
        def dp(start, end, k):                                                                    #DP the points from boxes[start:end + 1] with extra k boxes which is the same color with boxes[start] in the left side.
            if start > end:                                                                       #If start > end, return 0.
              return 0
            while start + 1 <= end and boxes[start] == boxes[start + 1]:                          #Increase both start and k if there are consecutive colors with boxes[start] in the beginning.
                start += 1
                k += 1
            points = (k + 1) ** 2 + dp(start + 1, end, 0)                                         #Calculate points of removing all boxes which has the same color with boxes[start], plus the points of remaining boxes[start + 1:end + 1]
            for i in range(start + 1, end + 1):                                                   #Traverse from start + 1 tp end.
                if boxes[start] == boxes[i]:                                                      #If boxes[i] == boxes[start], try remove boxes[start + 1:i](there is no boxes whose color is same with boxes[start + 1] before start + 1), then remove boxes[i:end + 1](there are k + 1 whose color is same with boxes[i], i.e. boxes[start]).
                    points = max(points, dp(start + 1, i - 1, 0) + dp(i, end, k + 1))             #Update max points.
            return points                                                                         #Return points.

        return dp(0, len(boxes) - 1, 0)                                                           #Top-down DP from the entire array.
