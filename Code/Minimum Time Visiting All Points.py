class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) for i in range(1, len(points)))      #The optimal strategy is to go diagonal as much as possible.
                                                                                                                                        #For 2 points whose distance is x on x axis and y on y axis.
                                                                                                                                        #We can go min(x, y) diagonal and the rest horizontal or vertical, which is abs(x - y).
                                                                                                                                        #Which is equivalant to max(x, y).
