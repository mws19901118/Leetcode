class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        prev_heights = []                                        #Initialize the height of 1 at each column at previous row.
        result = 0
        for row in matrix:                                       #Traverse each row.
            heights = []                                         #Initialize the height of 1 at each column at current row.
            seen = [False] * len(row)                            #Initialize if column with 1 from current row is seen on previous row.
            for height, i in prev_heights:                       #Traverse prev_heights.
                if row[i] == 1:                                  #If the cell at current row and same column, append height + 1 and i to heights. 
                    heights.append((height + 1, i))
                    seen[i] = True                               #Also set current column as seen.
            for i in range(len(row)):                            #Traverse each column.
                if seen[i] == False and row[i] == 1:             #If current cell is 1 and the column is not seen, appebd 1 and i to heights.
                    heights.append((1, i))                       #Since we always put the columns seen on last first, so the heights is sorted in desending order natually.
            for i in range(len(heights)):                        #Traverse heights.
                result = max(result, heights[i][0] * (i + 1))    #Calculate the submatrix whose botton right corner is current cell, the area is heights[i][0] * (i + 1) because after rearrangement, all columns before current cell has more 1.
            prev_heights = heights                               #Replace prev_heights with current height.
        return result
