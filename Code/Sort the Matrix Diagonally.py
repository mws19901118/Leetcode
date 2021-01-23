class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        startingPositions = [(i, 0) for i in range(len(mat))]                     #Enumerate the starting positions of each diagonal.
        startingPositions.extend([(0, i) for i in range(1, len(mat[0]))])
        for x, y in startingPositions:                                            #Traverse starting positions.
            diagonal = []
            i, j = x, y
            while i < len(mat) and j < len(mat[i]):                               #Traverse the diagonal and store numbers in a list.
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()                                                       #Sort list.
            for i in range(len(diagonal)):                                        #Update the values in diagonal.
                mat[x + i][y + i] = diagonal[i]
        return mat                                                                #Return matrix.
