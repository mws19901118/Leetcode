import copy
class Solution:
    def finished(self, board):                                                                              #Given the tuple representing the board, determine if game reaches the end.
        return all(board[i] == i + 1 for i in range(len(board) - 1))                                        #The ith element should be equal to i + 1, except the last element.
    
    def convertBoardToTuple(self, board):                                                                   #Covert the board from list of list to tuple.
        r = []
        for x in board:                                                                                     #Flatten the list of list.
            r.extend(x)
        return tuple(r)                                                                                     #Convert to tuple.
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        trace = set()                                                                                       #Use set to record trace.
        count = 0                                                                                           #Count number of moves.
        p = None
        for i in range(len(board)):                                                                         #Find the inital position of empty square.
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    p = (i, j)
        q = [(self.convertBoardToTuple(board), p)]                                                          #Store the current pattern of board, as a tuple of board tuple and white square position tuple.
        while q:                                                                                            #BFS.
            nextq = []                                                                                      #Next level.
            for x in q:
                b, c = x[0], x[1]                                                                           #Get board and white square postion.
                if self.finished(b):                                                                        #If board is in finished pattern, return count.
                    return count
                if b in trace:                                                                              #If board has already been passed, continue.
                    continue
                for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:                                                #Enumerate 4 directions.
                    newc = (c[0] + d[0], c[1] + d[1])                                                       #Calculate new position.
                    if newc[0] >= 0 and newc[0] < len(board) and newc[1] >= 0 and newc[1] < len(board[0]):  #If new positon is valid.
                        t = list(b)                                                                         #Convert board to a list.
                        t[c[0] * len(board[0]) + c[1]] = b[newc[0] * len(board[0]) + newc[1]]               #Swap the square of current position and new position.
                        t[newc[0] * len(board[0]) + newc[1]] = 0
                        nextq.append((tuple(t), newc))                                                      #Append current pattern of board, as a tuple of board tuple and white square position tuple, to nextq.
                trace.add(b)
            count += 1                                                                                      #Increase count by 1.
            q = nextq                                                                                       #Replace q with nextq.
        return -1                                                                                           #If cannot finish, return -1.
