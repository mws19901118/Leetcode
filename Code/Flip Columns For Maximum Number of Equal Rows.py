class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])                                                      #Get the n dimension of matrix.
        mask = (1 << n) - 1                                                     #Initialize mask to be all 1 of a row.
        count = Counter(int("".join([str(x) for x in r]), 2) for r in matrix)   #Convert each row to a binary string then to a integer; next count each integer.
        return max(count[x] + count[mask ^ x] for x in count)                   #Return the max result of count[x] + count[mask ^ x], which means 2 type of rows whose binary integer OR result is all 1, so after some operations, they can be flipped to all 0 or all 1.
