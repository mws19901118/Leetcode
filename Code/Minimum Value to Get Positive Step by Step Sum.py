class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minValue, psum = 0, 0                 #Initialize min value and prefix sum.
        for x in nums:                        #Traverse nums.
            psum += x                         #Update psum.
            minValue = min(minValue, psum)    #Update min value for psum.
        return -minValue + 1                  #Return -minValue + 1.
