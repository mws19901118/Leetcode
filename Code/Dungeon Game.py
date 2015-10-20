class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        row=len(dungeon)
        column=len(dungeon[0])
        HP=[[1 for i in range(column)] for i in range(row)]
        for i in range(row):
            for j in range(column):
                if i==0 and j==0:
                    HP[row-1-i][column-1-j]=max(HP[row-1-i][column-1-j]-dungeon[row-1-i][column-1-j],1)       #For the bottom-right corner, HP[i][j]=max(1-dungeon[i][j],1)
                elif i==0 and j!=0:
                    HP[row-1-i][column-1-j]=max(HP[row-1-i][column-j]-dungeon[row-1-i][column-1-j],1)         #For the bottom line, HP[i][j]=max(HP[i][j+1]-dungeon[i][j],1)
                elif i!=0 and j==0:
                    HP[row-1-i][column-1-j]=max(HP[row-i][column-1-j]-dungeon[row-1-i][column-1-j],1)         #For the right line, HP[i][j]=max(HP[i+1][j]-dungeon[i][j],1)
                else:
                    HP[row-1-i][column-1-j]=max(min(HP[row-1-i][column-j],HP[row-i][column-1-j])-dungeon[row-1-i][column-1-j],1)  #For any cell else, HP[i][j]=max(min(HP[i][j+1],HP[i+1][j])-dungeon[i][j],1)
        return HP[0][0]         #Return the min HP of starting cell.
