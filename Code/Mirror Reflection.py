class Solution:
    def findReflectPoint(self, point: tuple, k: float, line: tuple) -> tuple:       #Find the reflection point.
        b = point[1] - k * point[0]                                                 #Calculate the b of y = k * x + b.
        if line[0]:                                                                 #If line is vertical, the reflection point should be (x, k * x + b), x = 0 or p.
            return (line[1], k * line[1] + b)
        else:                                                                       #If line is horizontal, the reflection point should be ((y - b) / k), y), y = 0 or p.
            return ((line[1] - b) / k, line[1])
    def mirrorReflection(self, p: int, q: int) -> int:
        point = (0, 0)                                                              #Initialize current point.
        lines = [(True, p), (False, p), (True, 0), (False, 0)]                      #Store the 4 edges of square. The first boolean means if it's vertical.
        i = 0                                                                       #Start with the first edge.
        k = q / p                                                                   #Calculate k.
        while True:
            nextp = self.findReflectPoint(point, k, lines[i])                       #Find reflection point.
            i = (i + 1) % 4                                                         #Go to next edge.
            if nextp[0] < 0 or nextp[0] > p or nextp[1] < 0 or nextp[1] > p:        #If this reflection point is invalid, continue.
                continue
            else:
                point = nextp                                                       #Update current point.
                k = -k                                                              #Update k to -k after reflection.
            
            if abs(point[0] - p) < 0.001 and abs(point[1]) < 0.001:                 #If reaches receptor 0, return 0.
                return 0
            elif abs(point[0] - p) < 0.001 and abs(point[1] - p) < 0.001:           #If reaches receptor 1, return 1.
                return 1
            elif abs(point[0]) < 0.001 and abs(point[1] - p) < 0.001:               #If reaches receptor 2, return 2.
                return 2
                
from fractions import gcd
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)                                                               #In general, the ray goes to the first integer point (kp, kq) where k is an integer, and kp and kq are multiples of p.
        p = (p / g) % 2                                                             #Thus, the goal is just to find the smallest k for which kq is a multiple of p.
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2                                      #The mathematical answer is k = p / gcd(p, q).
