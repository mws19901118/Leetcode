class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def backtrack(i,j,k):               #Backtracking search; i,j is the coordinate of current character in board and k is the index of current character in word.
            if (i,j) in stack or (i<0 or i>=row or j<0 or j>=column) or board[i][j]!=word[k]:     #If coordinate is out of bound or coordinate has aleardy been in the path or the character in board doesn't match the character in word, return false.
                return False
            else:
                stack.append((i,j))         #Append current coordinate to the stack.
                if k==n-1:                  #If find the word, return true.
                    return True
                else:
                    if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):    #Search the adjcent characters.  
                        return True
                    else:
                        stack.pop()         #If can not find the word, pop stack and return false.
                        return False
        
        row=len(board)
        if row==0:
            return False
        column=len(board[0])
        if column==0:
            return False
        n=len(word)
        if n==0:
            return False
        for i in range(row):
            for j in range(column):
                stack=[]                            #Record the path of backtracking search.
                if backtrack(i,j,0):                #If find word, return true.
                    return True
        return False                                #If can not find word, return false.
