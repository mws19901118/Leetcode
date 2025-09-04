class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance1, distance2 = abs(x - z), abs(y - z)                                      #Calculate the distance from x to z and from y to z.
        return 0 if distance1 == distance2 else (1 if distance1 < distance2 else 2)        #Return result based on the relations of 2 distances.
