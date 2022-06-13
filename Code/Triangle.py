class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        level = triangle[0]                                                                                                                                                             #Record the minimum path sum at current row, initially it's the first row of triangle.
        for i in range(1, len(triangle)):                                                                                                                                               #Traverse triangle by level.
            nextLevel = [level[0] + triangle[i][0]] + [triangle[i][j] + min(level[j - 1], level[j]) for j in range(1, len(triangle[i]) - 1)] + [level[-1] + triangle[i][-1]]            #Updatet the minimal path sum at next level.
            level = newLevel                                                                                                                                                            #Replace level with nextLevel.
        return min(level)                                                                                                                                                               #Return minumum number in level.
