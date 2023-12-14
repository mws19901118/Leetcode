class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow, onesCol = [sum(x) for x in grid], [sum(x) for x in zip(*grid)]                                                                   #Calculate onesRow and onesCol.
        return [[2 * onesRow[i] + 2 * onesCol[j] - len(onesCol) - len(onesRow) for j in range(len(onesCol))] for i in range(len(onesRow))]        #Calculate diff matrix based on onesRow and onesCol then return.
