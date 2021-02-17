class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:                                                                 #Use 2 bars from both ends traversing towards middle.
            result = max(result, min(height[left], height[right]) * (right - left))         #Update result if current area is greater.
            if height[left] < height[right]:                                                #If right bar is higher than the left bar, we don't need to move right bar until left bar is higher than the right bar and vise versa.
                left += 1
            else:
                right -= 1
        return result
