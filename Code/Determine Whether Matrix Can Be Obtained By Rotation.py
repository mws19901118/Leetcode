class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return all(target[i][j] == mat[i][j] for i, j in product(range(len(mat)), range(len(mat)))) or all(target[i][j] == mat[j][len(mat) - 1 - i] for i, j in product(range(len(mat)), range(len(mat)))) or all(target[i][j] == mat[len(mat) - 1 - i][len(mat) - 1 - j] for i, j in product(range(len(mat)), range(len(mat)))) or all(target[i][j] == mat[len(mat) - 1 - j][i] for i, j in product(range(len(mat)), range(len(mat))))    #Check if target is mat rotating 0, 1, 2, or 3 times.
