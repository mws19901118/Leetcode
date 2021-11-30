class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:                                         #If matrix is not valid, return 0.
            return 0
        m, n = len(matrix), len(matrix[0])                                      #Get dimensions.
        height = [0] * (n + 1)                                                  #Record the accumulate heights of each column top-down. The length is column plus 1 to deal with the situation that the sequence of height is a non-descending sequence.
        maxarea = 0
        for i in range(m):                                                      #Traverse each row.
            stack = []                                                          #Store the indexes of asending heights; pop stack when encounter a height smaller than the height of index on the top of stack until the heights stored in stack is ascending.
            for j in range(n + 1):
                if j < n:
                    height[j] = height[j] + 1 if matrix[i][j] == '1' else 0     #If current character is '1', the accumulate height at current column increased by 1; otherwise, set it to 0.
                while stack and height[j] <= height[stack[-1]]:                 #While the height of index on the top of stack is larger than current height, keep pop the stack until the stack is empty.
                    h = height[stack.pop()]                                     #All the heights which are stored in the stack(not the top of stack) are smaller than height of column index on the top of stack. Thus, let it be not only the left boundry(if stack is not empty) but also the height of current rectangle.
                    w = j if not stack else j - stack[-1] - 1                   #If stack is empty, width is column index of current height; otherwise, width is the distance between current height and the column index on the top of stack.
                    maxarea = max(maxarea, w * h)                               #Calculate the area of current rectangle and update max area if necessary.
                stack.append(j)                                                 #Push current column index to stack.
        return maxarea
