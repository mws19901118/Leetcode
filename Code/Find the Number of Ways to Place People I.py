class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (-x[1], x[0]))       #Sort from top to bottom then from left to right.
        result = 0
        for i, (x, y) in enumerate(points):              #Traverse points as the top left corner.
            max_x = inf                                  #Initialize the max x value.
            for u, v in points[i + 1:]:                  #Traversepoints[i + 1:] the the bottom right corner.
                if x <= u:                               #If x <= u, we found a candidate because we know y is greater than or equal to v.
                    if u < max_x:                        #If u < max_x, there is no points in between, so increase result.
                        result += 1
                    max_x = min(u, max_x)                #Update the max_x visited.
                else:                                    #Otherwise, skip.
                    continue
        return result
