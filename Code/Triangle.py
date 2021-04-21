class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        level = triangle[0]                                                         #Record the minimum path sum at current row, initially it's the first row of triangle.
        for i in range(1, len(triangle)):                                           #Traverse triangle by level.
            newLevel = [level[0] + triangle[i][0]]                                  #Initialize the minimum path sum at this level with leftmost path sum.
            for j in range(1, len(triangle[i]) - 1):                                #Calculate the minimim path sum at this level for number not at either side and append.
                newLevel.append(triangle[i][j] + min(level[j - 1], level[j]))
            newLevel.append(level[-1] + triangle[i][-1])                            #Append the rightmost minimum path sum.
            level = newLevel                                                        #Replace level with newLevel.
        return min(level)                                                           #Return minumum number in level.
