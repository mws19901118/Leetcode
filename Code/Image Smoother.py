class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])                                              #Get the dimensions of img.
        smoothed = [[0 for _ in range(n)] for _ in range(m)]                      #Initialize the smoothed img with same dimensions.
        for i, j in product(range(m), range(n)):                                  #Traverse img.
            total, count = 0, 0
            for x, y in product([i - 1, i, i + 1], [j - 1, j, j + 1]):            #Traverse the 3 x 3 matrix around current cell.
                if 0 <= x < m and 0 <= y < n:                                     #If current cell in 3 x 3 matrix is valid, add its value to total and increase count.
                    total += img[x][y]
                    count += 1
            smoothed[i][j] = total // count                                       #Update smoothed[i][j] to be the smoothed value.
        return smoothed
