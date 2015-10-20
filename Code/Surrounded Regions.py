class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def fill(x,y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y]!='O':
                return
            queue.append((x,y))                                     #add to queue
            board[x][y]='B'                                         #change unsurrounded 'O' to 'B' to distinguish it from surrounded 'O'
        def bfs(x,y):
            if board[x][y]=='O':
                queue.append((x,y))                                 #add to queue
                fill(x,y)
            while queue:
                temp=queue.pop(0)                                   #pop a tuple
                i=temp[0]
                j=temp[1]
                fill(i-1,j)
                fill(i+1,j)
                fill(i,j-1)
                fill(i,j+1)
        if board==[]:
            return
        m=len(board)                                                #get the length of colomn
        n=len(board[0])                                             #get the length of row
        queue=[]                                                    #queeu to record the consequence of tuple
        for i in range(n):                                          #bfs along edges
            bfs(0,i)
            bfs(m-1,i)
        for i in range(m):
            bfs(i,0)
            bfs(i,n-1)
        for i in range(m):                                          #change 'B' to 'O', 'O' to 'X'
            for j in range(n):
                if board[i][j]=='B':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
