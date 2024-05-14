class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def BFS(board: List[List[str]], coordinate: tuple) -> None:
            q = [coordinate]                                                                        #Initialize queue.
            board[coordinate[0]][coordinate[1]] = 'V'                                               #Set current cell to 'V'.
            while q:                                                                                #BFS.
                newq = []                                                                           #Initialize new queue.
                for x, y in q:                                                                      #Traverse coordinates in q.
                    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                 #Traverse neighbors of current cell.
                        if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == 'O':      #If neithbor is valid and is 'O', set neighbor to 'V' and append the corrdinate to newq.
                            board[nx][ny] = 'V'
                            newq.append((nx, ny))
                q = newq                                                                            #Replace q with newq.
                
        m, n = len(board), len(board[0])                                                            #Get the dimensions.
        for i, j in product(range(m), range(n)):                                                    #Traverse board.
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':               #If current cell is on the border and is 'O', start BFS at current cell and set all connected 'O' to 'V'.
                BFS(board, (i, j))
        for i, j in product(range(m), range(n)):                                                    #Traverse board.
            board[i][j] = 'O' if board[i][j] == 'V' else 'X'                                        #If current cell is 'V', set it to 'O'; otherwise, set it to 'X'.
