class Solution:
    def isSquare(self, v1: tuple, v2: tuple, v3: tuple) -> bool:                                                                    #Check if v1, v2, v3 is a valid square, when v1 and v2 are 2 edges starting from p1 and v3 is the diagonal.
        return (v1 != (0, 0) and ((-v1[1], v1[0]) == v2 or (v1[1], -v1[0]) == v2) and (v1[0] + v2[0], v1[1] + v2[1]) == v3)         #To be valid square, there are a few conditions.
                                                                                                                                    #1. v1 should not be 0 length; 2. v1 rotate 90 degree(either clockwise or counterclockwise) should be v2; 3. v1 + v2 should be v3.
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        v1, v2, v3 = (p2[0] - p1[0], p2[1] - p1[1]), (p3[0] - p1[0], p3[1] - p1[1]), (p4[0] - p1[0], p4[1] - p1[1])                 #Find the vectors from p1 to p2, p3 and p4, respectively.
        return self.isSquare(v1, v2, v3) or self.isSquare(v2, v3, v1) or self.isSquare(v3, v1, v2)                                  #Check if any combination of v1, v2, v3 can form a valid square.
