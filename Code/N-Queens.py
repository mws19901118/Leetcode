class Solution:
    def lock(self, board, x, y):                                    #Once a queen is placed, lock all the position conflicting with current queen by increasing board[x][y] by 1.        
        n=len(board)                                                
        board[x][y]=-1                                              #Set current coordinate to -1 indicationg there is a queen here.
        for i in range(x+1,n):                                      #Lock all the position in the down side of this column.
            board[i][y]+=1
        for i in range(0,y):                                        #Lock all the position in the left side of this row.
            board[x][i]+=1
        for i in range(y+1,n):                                      #Lock all the position in the right side of this row.
            board[x][i]+=1
        for i in range(min(n-1-x,y)):                               #Lock all the position in the lower left diagonal line.
            board[x+1+i][y-1-i]+=1
        for i in range(min(n-1-x,n-1-y)):                           #Lock all the position in the lower right diagonal line.
            board[x+1+i][y+1+i]+=1
        
    def unlock(self, board, x, y):                                  #Once a queen is removed, unlock all the position conflicting with current queen by decreasing board[x][y] by 1. It is the reverse process of 'lock'.
        n=len(board)
        board[x][y]=0
        for i in range(x+1,n):
            board[i][y]-=1
        for i in range(0,y):
            board[x][i]-=1
        for i in range(y+1,n):
            board[x][i]-=1
        for i in range(min(n-1-x,y)):
            board[x+1+i][y-1-i]-=1
        for i in range(min(n-1-x,n-1-y)):
            board[x+1+i][y+1+i]-=1
        
    def formString(self, board):                                    #Once a possible solution is found, convert board to a list of strings.
        n=len(board)
        result=[]
        for i in range(n):
            str=""
            for j in range(n):
                if board[i][j]==-1:
                    str+="Q"
                else:
                    str+="."
            result.append(str)
        return result

    def setQueen(self, ans, board, x, y):                           
        n=len(board)
        self.lock(board, x, y)                                      #Place a queen in current position and lock all the conflicting position.
        if x==n-1:                                                  #If current row is the last row, a solution is found.
            ans.append(self.formString(board))
        else:
            for i in range(n):
                if board[x+1][i]==0:
                    self.setQueen(ans, board, x+1, i)               #Enumerate every avaliable position in the next row.
        self.unlock(board, x, y)                                    #Remove current position and unlock all the conflicting position.
    
    # @return a list of lists of string
    def solveNQueens(self, n):
        ans=[]
        board=[[0 for i in range(n)] for j in range(n)]             #Since a position might conflict more than one queen, it can be locked more than one time. The value of board[x][y] represents the times it is locked.
        for i in range(n):
            self.setQueen(ans, board, 0, i)                         #At the beginning, enumerate every position in the first row.
        return ans
