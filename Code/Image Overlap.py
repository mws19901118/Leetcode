class Solution:
    def calculateOverlap(self, A: List[List[int]], B: List[List[int]], x: int, y: int) -> int:          #Calculate the number of overlapping positions for a given move. x is the distance of A moving down(if x is negative, A is moving up) and y is the distance of A moving right(if y is negative, A is moving left).
        count = 0
        for i in range(len(A) - abs(x)):                                                                #After move, there are only N - |x| rows that are overlapping.
            rowA = A[i + max(0, -x)][max(0, -y):len(A) - max(0, y)]                                     #Find the a overlapping row in A with overlapping columns.
            rowB = B[i + max(0, x)][max(0, y):len(A) - max(0, -y)]                                      #Find the a overlapping row in B with overlapping columns.
            for j in range(len(rowA)):                                                                  #Count overlap positions.
                if rowA[j] & rowB[j]:
                    count += 1
        return count
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        result = 0
        for i in range(-n + 1, n):                                                                      #Check all possible vertical move of A(N - 1 for moving up, N - 1 for moving down, 1 for not moving).
            for j in range(-n + 1, n):                                                                  #Check all possible horizontal move of A(N - 1 for moving left, N - 1 for moving right, 1 for not moving).
                result = max(result, self.calculateOverlap(A, B, i, j))
        return result
