class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        m, n = len(image), len(image[0])

        start, end = 0, x                                                       #Binary search in 4 directions for the rectangle edge.
        while start <= end:
            mid = (start + end) // 2
            if all(image[mid][i] == '0' for i in range(n)):
                start = mid + 1
            else:
                end = mid - 1
        up = start

        start, end = x, m - 1
        while start <= end:
            mid = (start + end) // 2
            if all(image[mid][i] == '0' for i in range(n)):
                end = mid - 1
            else:
                start = mid + 1
        down = end

        start, end = 0, y
        while start <= end:
            mid = (start + end) // 2
            if all(image[i][mid] == '0' for i in range(up, down + 1)):          #After found the horizontal bound, we can narrow down the scope when finding the vertical bound.
                start = mid + 1
            else:
                end = mid - 1
        left = start

        start, end = y, n - 1
        while start <= end:
            mid = (start + end) // 2
            if all(image[i][mid] == '0' for i in range(up, down + 1)):
                end = mid - 1
            else:
                start = mid + 1
        right = end

        return (down - up + 1) * (right - left + 1)
