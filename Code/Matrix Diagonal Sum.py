class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(mat[i][i] + mat[i][-(i + 1)] for i in range(len(mat))) - (mat[len(mat) // 2][len(mat) // 2] if len(mat) & 1 else 0)        #Sum 2 diagonals and substract number in the middle if length of matrix is odd.
