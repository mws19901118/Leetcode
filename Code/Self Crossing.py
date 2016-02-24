class Solution(object):
    def segmentCrossing(self, A, B, C, D):                                                                  #Judge if 2 segments crosses each other.
        if (A[0] - C[0]) * (B[0] - D[0]) <= 0 and (A[1] - C[1]) * (B[1] -D[1]) <= 0:
            return True
        if (A[0] - D[0]) * (B[0] - C[0]) <= 0 and (A[1] - D[1]) * (B[1] -C[1]) <= 0:
            return True
        return False
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        points = [(0, 0)]                                                                                   #Start at (0, 0).
        dire = [(0, 1), (-1, 0), (0, -1), (1, 0)]                                                           #Store 4 directions: north is +y; west is -x; south is -y; east is +x;
        for i in range(len(x)):
            points.append((points[-1][0] + dire[i%4][0] * x[i], points[-1][1] + dire[i%4][1] * x[i]))       #Generate new point by previous point and direction.
            if len(points) >= 7 and self.segmentCrossing(points[-7], points[-6], points[-2], points[-1]):   #Judge if the new segment crosses the last 3rd, 4th, 5th segments, if exist.
                return True
            if len(points) >= 6 and self.segmentCrossing(points[-6], points[-5], points[-2], points[-1]):
                return True
            if len(points) >= 5 and self.segmentCrossing(points[-5], points[-4], points[-2], points[-1]):
                return True
        return False
