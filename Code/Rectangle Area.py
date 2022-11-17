class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        horizontalOverlap = max(0, min(ax2, bx2) - max(ax1, bx1))                   #Calculate horizontal overlap.
        vertitalOverlap =  max(0, min(ay2, by2) - max(ay1, by1))                    #Calculate vertial overlap.
        area1 = (ax2 - ax1) * (ay2 - ay1)                                           #Calculate area of first rectangle.
        area2 = (bx2 - bx1) * (by2 - by1)                                           #Calculate area of second rectangle.
        return area1 + area2 - horizontalOverlap * vertitalOverlap                  #Calculate total rectangle area.
