class Solution:
    def trap(self, height: List[int]) -> int:
        count, left, right, leftMax, rightMax = 0, 0, len(height) - 1, 0, 0         #Initalize count, left point, right pointer, left max height and right max height.
        while left < right:                                                         #Traverse while left is smaller than right, the taller of left height and right height will always be the current max on corresponding side.
            if height[left] < height[right]:                                        #If left height is shorter than right height, the water trapped depends on the left height. 
                leftMax = max(leftMax, height[left])                                #Update left max height.
                count += leftMax - height[left]                                     #Add leftMax - height[left] to count.
                left += 1                                                           #Increase left pointer.
            else:                                                                   #Otherwise, the water trapped depends on the right height.
                rightMax = max(rightMax, height[right])                             #Update right max height.
                count += rightMax - height[right]                                   #Add rightMax - height[right] to count.
                right -= 1                                                          #Decrease right pointer.
        return count                                                                #Return count.

class Solution:
    def trap(self, height: List[int]) -> int:
        stack, count = [], 0                                                        #Initialize the index stack in which the height at each index is in descending order; also initialize count.
        for i, h in enumerate(height):                                              #Traverse height.
            prevHeight = 0                                                          #Intialize previouse height that is in stack and is smaller than current height.
            while stack and height[stack[-1]] <= h:                                 #While stack is not empty and the height of stack top is no larger than current height, handle the water trapped by current height and the height on top of stack, where current height is higher.
                x = stack.pop()                                                     #Pop stack. All the water trapped below height[x] is already added to count.
                count += (height[x] - prevHeight) * (i - x - 1)                     #Add the water trapped in the rectangle(height is height[x] - prevHeight and width is from x to i - 1) to count.
                prevHeight = height[x]                                              #Update prevHeight.
            if stack:                                                               #If stack is not empty, handle water trapped by current height and the height on top of stack, where current height is shorter.
                count += (h - prevHeight) * (i - stack[-1] - 1)                     #Add the water trapped in the rectangle(height is h - prevHeight and width is from top of stack to i - 1) to count.
            stack.append(i)                                                         #Append current index to stack.
        return count                                                                #Return count.
