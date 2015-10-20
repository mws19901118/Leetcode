class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):                           #The idea is similar to that of Largest Rectangle in Histogram.
        row=len(matrix)                                           #Record the amount of rows.
        if row==0:
            return 0
        column=len(matrix[0])                                     #Record the amout of columns.
        if column==0:
            return 0
        height=[0]*(column+1)                                     #Record the accumulate heights of each column top-down. The length is column plus 1 to deal with the situation that the sequence of height is a non-descending sequence.
        r=0
        for i in range(row):
            stack=[]                                              #Store the indexes of asending heights; pop stack when encounter a height smaller than the height of index on the top of stack until the heights stored in stack is ascending.
            for j in range(column+1):
                if j<column:
                    if matrix[i][j]=='1':                         #If current character is '1', the accumulate height at current column increased by 1; otherwise, set it to 0.
                        height[j]+=1
                    else:
                        height[j]=0
                        
                while stack and height[j] <=height[stack[-1]]:    #While the height of index on the top of stack is larger than current height, keep pop the stack until the stack is empty.
                    h = height[stack.pop()]                       #All the heights which are stored in the stack(not the top of stack) are smaller than height of column index on the top of stack. Thus, let it be not only the left boundry(if stack is not empty) but also the height of current rectangle.
                    w = j if not stack else j - stack[-1] -1      #If stack is empty, width is column index of current height; otherwise, width is the distance between current height and the column index on the top of stack.
                    r = max(r, w*h)                               #Calculate the area of current rectangle; if it's larger than max area, let it be the new max area.
                stack.append(j)                                   #Push current column index to stack.
        return r
