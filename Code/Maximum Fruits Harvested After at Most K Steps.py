class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        result, s, left = 0, 0, 0                                                                                          #Initialize result, fruit sum and left end of the sliding window(inclusive).
        
        def step(left: int, right: int) -> int:                                                                            #Calculate steps needed to visit all positions between index left and index right(inclusive) from start position.
            if fruits[right][0] <= startPos:                                                                               #If the position of fruits[right] is not greater than start position, just go left from start position so return startPos - fruits[left][0].
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:                                                                              #If the position of fruits[left] is not smaller than start position, just go right from start position so return fruits[right][0] - startPos.
                return fruits[right][0] - startPos
            return min(fruits[right][0] - startPos, startPos - fruits[left][0]) + fruits[right][0] - fruits[left][0]       #Otherwise, go both direction(fruits[right][0] - fruits[left][0]), but add the min value of going right first then come back((fruits[right][0] - startPos) and going left first then comback(startPos - fruits[left][0]).

        for i, [x, y] in enumerate(fruits):                                                                                #Traverse fruits to enumerate the right end of sliding window.
            s += y                                                                                                         #Add y to fruit sum. 
            while left <= i and step(left, i) > k:                                                                         #Iterate while left is not greater than i and the steps needed to visit all positions between index left and index i(inclusive) from start position is greater than k.
                s -= fruits[left][1]                                                                                       #Remove fruit at left from fruit sum.
                left += 1                                                                                                  #Move forward left.
            result = max(result, s)                                                                                        #Update result if necessary.
        return result
