class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)                                        #Append 0 in the end to deal with the situation that the sequence of height is a non-descending sequence.
        stack = [0]                                             #Store the indexes of asending heights; pop stack when encounter a height smaller than the height of index on the top of stack until the heights stored in stack is ascending.
        r = 0
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:      #While the height of index on the top of stack is larger than current height, keep pop the stack until the stack is empty.
                h = height[stack.pop()]                         #All the heights which are stored in the stack(not the top of stack) are smaller than height of index on the top of stack. Thus, let it be not only the left boundry(if stack is not empty) but also the height of current rectangle.
                w = i if not stack else i - stack[-1] -1        #If stack is empty, width is index of current height; otherwise, width is the distance between current height and the index on the top of stack.
                r = max(r, w*h)                                 #Calculate the area of current rectangle; if it's larger than max area, let it be the new max area.
            stack.append(i)                                     #Push current index to stack.
        return r
