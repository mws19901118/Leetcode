class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        delta = [[0 for _ in range(n + 1)] for _ in range(n)]        #Initialize the delta effect of all queries on each row.
        for r1, c1, r2, c2 in queries:                               #Traverse queries.
            for i in range(r1, r2 + 1):                              #Traverse from row r1 to row r2.
                delta[i][c1] += 1                                    #Increase 1 at column c1.
                delta[i][c2 + 1] -= 1                                #Decrease 1 at column c2 + 1.
        result = [[0 for _ in range(n)] for _ in range(n)]           #Initialize result.
        for i in range(n):                                           #Traverse each row.
            x = 0                                                    #Initialize value for currentrow.
            for j in range(n):                                       #Traverse each column.
                x += delta[i][j]                                     #Update value based on the delta effect.
                result[i][j] = x                                     #Update result at current coordinate.
        return result
