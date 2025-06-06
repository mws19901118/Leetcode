class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, q, visited, count = len(board), set([1]), set([1]), 0                  #Initialize n, q, visited and count.
        while q:                                                                  #BFS.
            newq = set()
            for x in q:                                                           #Traverse each label in q.
                if x == n * n:                                                    #If label is n ^ 2, we reach the end so return count.
                    return count
                for y in range(x + 1, min(x + 6, n * n) + 1):                     #Roll the dice and move forward 1 to 6 steps(keep within the range of 1 to n ^ 2).
                    row, col = divmod(y - 1, n)                                   #Get the row and col of label if board is a normal matrix.
                    row, col = n - row - 1, n - 1 - col if row & 1 else col       #But since it's Boustrophedon style, count row from bottom and count column from the direction based on the parity of row.
                    target = y if board[row][col] == -1 else board[row][col]      #If it is start of ladder or snake, set the target to the end of ladder or snake; otherwise, set the target to itself.
                    if target not in visited:                                     #If target is not visited, add target to newq.
                        newq.add(target)
            q = newq                                                              #Replace q with newq.
            visited |= newq                                                       #Mark of newq as visited.
            count += 1                                                            #Increase count.
        return -1                                                                 #Return -1 if cannot reach n ^ 2.
