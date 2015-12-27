class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        x = []                                                      #Store the x coordinate of people.
        y = []                                                      #Store the y coordinate of people.
        count = 0                                                   #Count the number of people.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
                    count += 1
        x.sort()                                                    #Sort, then find median.
        y.sort()                                                    #Sort, then find median.
        if count % 2 == 1:
            medianx = x[count / 2]
            mediany = y[count / 2]
        else:
            medianx = int((x[count / 2 - 1] + x[count / 2]) / 2)
            mediany = int((y[count / 2 - 1] + y[count / 2]) / 2)
        distance = 0
        for i in range(count):                                      #Calculate the sum of Manhattan distance.
            distance += abs(x[i] - medianx) + abs(y[i] - mediany)
        return distance
