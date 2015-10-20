class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        def findRight(i):                                         #Find the right wing of an height, including itself.
            right=1
            j=i+1
            while j<n and height[j]>=height[i]:                   #Calculate right wing iteratively.
                right+=rdict[j]                                   #The increasement of right wing equals to the right wing of j.
                j+=rdict[j]                                       #Let the height on the right of right wing of j be the new j.
            rdict[i]=right
            return right
        
        def findLeft(i):                                          #Find the left wing of an height, including itself.
            if i+1<n and height[i]==height[i+1]:                  #Deal with the situation that current height equals the next one.
                ldict[i]=ldict[i+1]-1                             #Left wing of current height equals to the left wing of next height minus 1.
                return ldict[i]
            j=i-1
            while j>=0 and height[j]>=height[i]:                  #Calculate the left wing.
                j-=1
            ldict[i]=i-j
            return i-j
        
        n=len(height)
        if n==0:
            return 0
        rdict={}                                                  #Dictionary to record the right wings.                  
        ldict={}                                                  #Dictionary to record the left wings.
        minHeight=min(height)
        maxArea=n*minHeight                                       #The least value of max area.
        i=n-1
        while i>=0:
            currentArea=(findRight(i)+findLeft(i)-1)*height[i]    #Caculate the area of current rectangle(Because both left wing and right wing contain current height itself, the result should eliminate duplicate).
            if currentArea>maxArea:
                maxArea=currentArea
            i-=1
        return maxArea


#However, my solution is not efficient enough; it will get TLE if I traverse in the reverse direction. Here is a better solution:

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
