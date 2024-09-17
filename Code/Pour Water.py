class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        leftFall, rightFall = [], []                                                                            #Use leftFall and rightFall to store the indexes whose heights is smaller than previous index during water flowing from k to left and right respectively. 
        leftBoundary, rightBoundary = k, k                                                                      #Use leftBounday and rightBoundary to store the farest index the water can flow without reaching a higher height from k to left and right respectively.
        for _ in range(volume):                                                                                 #Pour water once a time.
            while leftBoundary > 0 and heights[leftBoundary - 1] <= heights[leftBoundary]:                      #While water can flow left. decrease leftBoudary.
                leftBoundary -= 1
                if heights[leftBoundary] < heights[leftBoundary + 1]:                                           #If heights[leftBoundary] is smaller than previous one, water will fall downward, so append leftBoundary to leftFall.
                    leftFall.append(leftBoundary)
            while rightBoundary < len(heights) - 1 and heights[rightBoundary + 1] <= heights[rightBoundary]:    #While water can flow right. increase rightBoudary.
                rightBoundary += 1
                if heights[rightBoundary] < heights[rightBoundary - 1]:                                         #If heights[rightBoudary] is smaller than previous one, water will fall downward, so append rightBoudary to leftFall.
                    rightFall.append(rightBoundary)
            if leftFall:                                                                                        #If leftFall is not empty, water will flow to leftFall[-1] and accumulate at there.
                leftmostFall = leftFall[-1]
                heights[leftmostFall] += 1                                                                      #Increase heights[leftmostFall].
                if heights[leftmostFall] == heights[leftmostFall + 1]:                                          #If the height equals prevopis one, water cannot fall here anymore, so pop leftFall.
                    leftFall.pop()
                if leftmostFall > leftBoundary:                                                                 #If this is not leftBoundary yet, there are more indexes between leftmostFall and leftBoundary where water will fall, so append leftmostFall - 1 to leftFall.
                    leftFall.append(leftmostFall - 1)
            elif rightFall:                                                                                     #If rightFall is not empty, water will flow to rightFall[-1] and accuulate at there.
                rightmostFall = rightFall[-1]
                heights[rightmostFall] += 1                                                                     #Increase heights[rightmostFall].
                if heights[rightmostFall] == heights[rightmostFall - 1]:                                        #If the height equals prevopis one, water cannot fall here anymore, so pop rightFall.
                    rightFall.pop()
                if rightmostFall < rightBoundary:                                                               #If this is not rightBoundary yet, there are more indexes between rightmostFall and rightBoundary where water will fall, so append rightmostFall - 1 to rightFall.
                    rightFall.append(rightmostFall + 1)
            else:                                                                                               #Otherwise, water will accumulate at k.
                heights[k] += 1
                if k > leftBoundary:                                                                            #If k is greater than leftBoundary now, append k - 1 to leftFall because next water flow left will start to fall from here.
                    leftFall.append(k - 1)
                if k < rightBoundary:                                                                           #If k is smaller than rightBoundary now, append k + 1 to rightFall bcause next water flow right will start to fall from here.
                    rightFall.append(k + 1)
        return heights
