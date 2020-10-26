class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]                                                          #Initialize the first row with poured.
        for i in range(query_row):                                              #Simulating the flow for each row.
            nextRow = [0] * (len(row) + 1)                                      #Intialize next row with all glasses empty.
            for j in range(len(row)):
                overflow = (max(row[j] - 1, 0)) / 2                             #For each cup, calculate the amount overflowed to next row.
                nextRow[j] += overflow                                          #Add overflow to the left glass in next row.
                nextRow[j + 1] += overflow                                      #Add overflow to the right glass in next row.
            row = nextRow                                                       #Replace current row with next row.
        return min(1, row[query_glass])                                         #Return the amout in query glass, maximum is 1. 
