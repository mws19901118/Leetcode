class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        l=len(height)
        area=0
        if l<1:
            return 0
        left=0
        right=l-1
        while left<right:                                         #We can check the left and right alternatively. When left bar pass right bar, we've already check all the boundaries.
            if min(height[left],height[right])*(right-left)>area:
                area=min(height[left],height[right])*(right-left)
            if height[left]>height[right]:                        #If left bar is higher than the right bar, we don't need to move left bar until right bar is higher than the left bar, vise versa.
                right-=1
            else:
                left+=1
        return area
