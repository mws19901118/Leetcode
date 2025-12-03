class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pairs = defaultdict(Counter)                                    #Count points pairs by the slope then by intercept.
        midpoints = defaultdict(Counter)                                #Count mid point of points pair by mid point coordinate then by slope of points pair.
        for i, (x, y) in enumerate(points):                             #Traverse points.
            for u, v in points[i + 1:]:                                 #Traverse points[i + 1:] so we are enumerating points pair.
                k, b = inf, x                                           #Initialize slope and intercept to be a vertical line.
                if x != u:                                              #If x != u, then calculate the real slope and intercept.
                    k = (v - y) / (u - x)
                    b = (y * (x - u)- x * (y - v)) / (x - u)            #When calculating intercept, avoid using calculated slope directly which might lead to a float precision issue.
                pairs[k][b] += 1                                        #Increase the count of current slope and intercept.
                midpoints[((x + u) / 2, (y + v) / 2)][k] += 1           #Increase the count of current mid point and slope.
        result = 0
        for k in pairs:                                                 #Traverse slopes.
            s = 0                                                       #Calculate the number of trapezoids which shares current parallel slope using the method in Count Number of Trapezoids I.
            for c in pairs[k].values():
                result += c * s
                s += c
        for (x, y) in midpoints:                                        #Traverse mid points.
            s = 0                                                       #There might be parallelograms such that are counted twice. For parallelograms, the mid points of 2 diagonal points pair have same coordinates but different slopes.
            for c in midpoints[(x, y)].values():                        #Thus, use the same technique again to remove double counted parallelograms.
                result -= c * s
                s += c
        return result
