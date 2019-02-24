class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        for i in range(V):
            j = K - 1                                                           #Search left to find the place for eventually fall.
            minHeight = heights[K]
            leftTarget = -1
            while j >= 0 and heights[j] <= heights[j + 1]:                      #j goes backward while heights[j] is smaller than or equal to heights[j + 1].
                if heights[j] < minHeight:                                      #The actual index of eventually fall should be strict smaller than the next height.
                    minHeight = heights[j]
                    leftTarget = j
                j -= 1
            if leftTarget != -1:                                                #If we can find a place to fall, add 1 to the height there.
                heights[leftTarget] += 1
            else:                                                               #Otherwise, search right to find the place for eventually fall.
                j = K + 1
                minHeight = heights[K]
                rightTarget = -1 
                while j < len(heights) and heights[j] <= heights[j - 1]:        #j goes forward while heights[j] is smaller than or equal to heights[j - 1].
                    if heights[j] < minHeight:                                  #The actual index of eventually fall should be strict smaller than the previous height.                           
                        minHeight = heights[j]
                        rightTarget = j
                    j += 1
                if rightTarget != -1:                                           #If we can find a place to fall, add 1 to the height there.
                    heights[rightTarget] += 1
                else:                                                           #Otherwise, add 1 to the height in K.
                    heights[K] += 1
        return heights
