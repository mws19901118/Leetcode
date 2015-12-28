class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0
        
        start = 0                                   #Binary search in 4 directions for the rectangle edge.
        end = x
        while start <= end:
            mid = (start + end) / 2
            black = False
            for i in range(n):
                if image[mid][i] == '1':
                    black = True
                    break
            if black is True:
                end = mid - 1
            else:
                start = mid + 1
        up = start

        start = x
        end = m - 1
        while start <= end:
            mid = (start + end) / 2
            black = False
            for i in range(n):
                if image[mid][i] == '1':
                    black = True
                    break
            if black is True:
                start = mid + 1
            else:
                end = mid - 1
        down = end

        start = 0
        end = y
        while start <= end:
            mid = (start + end) / 2
            black = False
            for i in range(up, down + 1):         #After found the horizontal bound, we can narrow down the scope when finding the vertical bound.
                if image[i][mid] == '1':
                    black = True
                    break
            if black is True:
                end = mid - 1
            else:
                start = mid + 1
        left = start

        start = y
        end = n - 1
        while start <= end:
            mid = (start + end) / 2
            black = False
            for i in range(up, down + 1):
                if image[i][mid] == '1':
                    black = True
                    break
            if black is True:
                start = mid + 1
            else:
                end = mid - 1
        right = end

        return (down - up + 1) * (right - left + 1)
