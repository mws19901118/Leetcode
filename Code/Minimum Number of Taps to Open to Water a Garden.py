class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxReach = [0] * (n + 1)                                                    #Store the maximum reach from each position.
        for i, x in enumerate(ranges):                                              #Traverse ranges.
            maxReach[max(0, i - x)] = max(maxReach[max(0, i - x)], min(n, i + x))   #Update the maximum reach for the leftmost position.
        count, currReach, nextReach = 0, 0, 0                                       #Initialize taps count, current rightmost position reached and next rightmost position that can be reached.
        for i in range(n + 1):                                                      #Traverse the taps from 1 to n.
            if i > nextReach:                                                       #If current postition cannot be reached, return -1 because the place between current tap and previous tap cannot be watered.
                return -1
            if i > currReach:                                                       #Increase tap when moving to a new tap beyond current reach.
                count += 1
                currReach = nextReach                                               #Now next rightmost position that can be reached becomes current rightmost position reached.
            nextReach = max(nextReach, maxReach[i])                                 #Update the next rightmost position that can be reached
        return count
