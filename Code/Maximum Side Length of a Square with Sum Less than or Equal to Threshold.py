class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])                                                                                                                                                                                                                                #Get the dimensions.
        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]                                                                                                                                                                                                           #Initialize prefix sum.
        for i, j in product(range(m), range(n)):                                                                                                                                                                                                                    #Populate prefix sum.
            prefixSum[i + 1][j + 1] = mat[i][j] + prefixSum[i + 1][j] + prefixSum[i][j + 1] - prefixSum[i][j]

        @cache                                                                                                                                                                                                                                                      #Cache result.
        def squareExist(length: int) -> bool:                                                                                                                                                                                                                       #Check if there exists a square with a sum less than or equal to threshold and given side length.
            return any(i + 1 >= length and j + 1 >= length and prefixSum[i + 1][j + 1] - prefixSum[i + 1 - length][j + 1] - prefixSum[i + 1][j + 1 - length] + prefixSum[i + 1 - length][j + 1 - length] <= threshold for i, j in product(range(m), range(n)))      #Traverse each cell and check the square(if exist) whose bottom right point is on current cell and sum is less than or equal to threshold.

        start, end = 1, min(m, n)                                                                                                                                                                                                                                   #Binary search max side length from 1 to min(m, n).
        while start <= end:
            mid = (start + end) // 2
            if squareExist(mid) and not squareExist(mid + 1):
                return mid
            elif squareExist(mid + 1):
                start = mid + 1
            else:
                end = mid - 1
        return 0                                                                                                                                                                                                                                                    #Return 0 if no such sqaure found.
