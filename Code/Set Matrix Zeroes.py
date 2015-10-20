class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row=len(matrix)
        if row==0:
            return False
        column=len(matrix[0])
        if column==0:
            return False
        sign=0xFFFFFFFF                                           #A rare value of integer to indicate the integer below a 0.
        for i in range(row):
            flag=False                                            #Initially, the current row should not be set to 0.
            for j in range(column):
                if matrix[i][j]==0:                               #If current integer is 0, set flag to True, set all the integers above it to 0 and set the integer(If have) below it to sign.
                    if i+1<row and matrix[i+1][j]!=0:
                        matrix[i+1][j]=sign
                    flag=True
                    for k in range(i):
                        matrix[k][j]=0
                if matrix[i][j]==sign:                            #If current integer is below a 0, set it to 0 and set the integer(If have) below it to sign.
                    if i+1<row and matrix[i+1][j]!=0:
                        matrix[i+1][j]=sign
                    matrix[i][j]=0
            if flag==True:                                        #If find a 0 in current row, set the whole row to 0.
                for j in range(column):
                    matrix[i][j]=0
