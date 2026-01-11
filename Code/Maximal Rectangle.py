class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea, n = 0, len(matrix[0])                                          #Initialize maxArea and get the length of each row.
        height = [0] * (n + 1)                                                  #Record the accumulate heights of each column top-down. The length is column plus 1 to deal with the situation that the sequence of height is a non-descending sequence.
        for row in matrix:                                                      #Traverse each row.
            stack = []                                                          #Store the indexes of asending heights; pop stack when encounter a height smaller than the height of index on the top of stack until the heights stored in stack is ascending.
            for i in range(n + 1):
                height[i] = height[i] + 1 if i < n and row[i] == '1' else 0                       
                while stack and height[i] <= height[stack[-1]]:                 #While the height of index on the top of stack is larger than current height, keep pop the stack until the stack is empty.
                    h = height[stack.pop()]                                     #All the heights which are stored in the stack(not the top of stack) are smaller than height of column index on the top of stack. Thus, let it be not only the left boundry(if stack is not empty) but also the height of current rectangle.
                    w = i if not stack else i - stack[-1] - 1                   #If stack is empty, width is column index of current height; otherwise, width is the distance between current height and the column index on the top of stack.
                    maxArea = max(maxArea, w * h)                               #Calculate the area of current rectangle; if it's larger than max area, let it be the new max area.
                stack.append(i)                                                 #Push current column index to stack.
        return maxArea
