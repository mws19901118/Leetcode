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
