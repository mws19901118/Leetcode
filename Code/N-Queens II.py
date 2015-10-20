class Solution:
    def lock(self, board, x, y):                              #Most code is the same with N-Queen.
        n=len(board)
        board[x][y]=-1
        for i in range(x+1,n):
            board[i][y]+=1
        for i in range(0,y):
            board[x][i]+=1
        for i in range(y+1,n):
            board[x][i]+=1
        for i in range(min(n-1-x,y)):
            board[x+1+i][y-1-i]+=1
        for i in range(min(n-1-x,n-1-y)):
            board[x+1+i][y+1+i]+=1
        
    def unlock(self, board, x, y):
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


    def setQueen(self, ans, board, x, y):
        n=len(board)
        self.lock(board, x, y)
        if x==n-1:
            ans[0]+=1
        else:
            for i in range(n):
                if board[x+1][i]==0:
                    self.setQueen(ans, board, x+1, i)
        self.unlock(board, x, y)
    
    # @return a list of lists of string
    def totalNQueens(self, n):
        ans=[0]                                             #Because I can not modify a number in method, use a list which has only one element counting the total number.
        board=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            self.setQueen(ans, board,0,i)
        return ans[0]
