class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])                                                #Get dimensions.
        coordinates = {mat[i][j]: (i, j) for i, j in product(range(m), range(n))}   #Build a dictionary mapping each number to its coordinate.
        countRow, countColumn = Counter(), Counter()                                #Count painted cells in each row and column.
        for i, x in enumerate(arr):                                                 #Traverse arr.
            coordinate = coordinates[x]                                             #Get coordinate of current number.
            countRow[coordinate[0]] += 1                                            #Increase count of its row.
            countColumn[coordinate[1]] += 1                                         #Increase count of its column.
            if countRow[coordinate[0]] == n or countColumn[coordinate[1]] == m:     #If either row or column is all painter, return current index.
                return i
