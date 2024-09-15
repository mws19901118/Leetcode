class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def serialize(matrix: List[List[str]]) -> str:                                                #Serialize board to string.
            return "".join([str(x) for x in matrix[0]] + [str(x) for x in matrix[1]])

        def deserialize(s: str) -> List[List[int]]:                                                   #Deserialize board from string.
            matrix = [[0, 0, 0], [0, 0, 0]]
            for i, j in product(range(2), range(3)):
                matrix[i][j] = int(s[i * 3 + j])
            return matrix

        x, y = -1, -1                                                                                 #Find the initial position of 0.
        for i, j in product(range(2), range(3)):
            if not board[i][j]:
                x, y = i, j
                break
        q = [(x, y, serialize(board))]
        visited = set([q[0][2]])
        moves = 0
        while q:                                                                                      #BFS.
            newq = []
            for x, y, s in q:                                                                         #Traverse q,
                if s == "123450":                                                                     #If s is the target state, return moves.
                    return moves
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                         #Traverse 4 neighbors.
                    if u < 0 or u >= 2 or v < 0 or v >= 3:                                            #If neighbor is invalid, continue. 
                        continue
                    currBoard = deserialize(s)                                                        #Deserialize board.
                    currBoard[u][v], currBoard[x][y] = currBoard[x][y], currBoard[u][v]               #Perform swap with neighbor.
                    new_s = serialize(currBoard)
                    if new_s in visited:                                                              #If the new board is visited, continue.
                        continue
                    visited.add(new_s)                                                                #Mark new board as visited.
                    newq.append((u, v, new_s))                                                        #Append neighbor and new board to newq.
            q = newq
            moves += 1
        return -1                                                                                     #Return -1 if cannot reach target state.
