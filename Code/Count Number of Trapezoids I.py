class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        count = Counter()                                  #Count points by y coordinate.
        for x, y in points:
            count[y] += 1
        result, s, division = 0, 0, 10 ** 9 + 7            #Initialize result, sum of pairs and division.
        for x in count.values():                           #Traverse the values of count.
            pairs = x * (x - 1) // 2                       #For current y coordinates, there are x * (x - 1) // 2 pairs of points .
            result = (result + pairs * s) % division       #Each pair will form a trapezoid with each visited pair.
            s += pairs                                     #Add pairs to s to update pairs count.
        return result
