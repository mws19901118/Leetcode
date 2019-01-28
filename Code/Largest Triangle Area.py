import itertools                                                                                        #Import itertools to get combinations from a list.
class Solution(object):
    def calculateArea(self, p0, p1, p2):                                                                #Calculete triangle area based on coordinates of each point.
        area = 0.5 * abs(p0[0] * (p1[1] - p2[1]) + p1[0] * (p2[1] - p0[1]) + p2[0] * (p0[1] - p1[1]))
        return area
    
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max(self.calculateArea(*triangle) for triangle in itertools.combinations(points, 3))     #Enumerate every triagnle and return the max.
