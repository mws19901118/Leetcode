class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        result = 0
        rooks.sort(key = lambda x: x[0])        #Sort rooks by row.
        for i, [x, y] in enumerate(rooks):      #Traverse rooks.
            result += abs(x - i)                #Put each rook on row 0 to n - 1 in order, since rooks are sorted by row, this will give the minimum moves to put rooks on each row.
        rooks.sort(key = lambda x: x[1])        #Sort rooks by column.
        for i, [x, y] in enumerate(rooks):      #Traverse rooks.
            result += abs(y - i)                #Put each rook on column 0 to n - 1 in order, since rooks are sorted by column, this will give the minimum moves to put rooks on each column.
        return result
