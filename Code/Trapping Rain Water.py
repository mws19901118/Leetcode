class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        l=len(height)
        if l<=2:                                                  #To trap water, length of integers should be at least 3.
            return 0
        
        sum=0                                                     #Record the total water trapped volume.
        i=0                                                       #This is the first pointer.
        while i<l:
            j=1                                                   #This is the second pointer.
            temp=0                                                #Record current trapped water volume.
            maxh=0                                                #Record the max height of integer behind i.
            maxgap=j                                              #Record the distance betweem maxh and i.
            maxcurrenttrap=0                                      #Record the current trapped water when traverse reaches maxh(excluded).
            while i+j<l and height[i+j]<height[i]:
                if height[i+j]>=maxh:                             #Find the maxh(as rear as possible), and then update maxh, maxg and maxcurrenttrap.
                    maxh=height[i+j]
                    maxg=j
                    maxcurrenttrap=temp
                temp+=height[i]-height[i+j]                       #Calculate current trapped water volume.
                j+=1
            if i+j==l:                                            #If reaches the end, the delta sum is maxcurrenttrap minus the area of void rectangle above current valid trapped water whose height is height[i]-maxh and width is maxg-1.
                sum+=maxcurrenttrap-(maxg-1)*(height[i]-maxh)
                i+=maxg                                           #Continue traverse at i+maxg.
            else:                                                 #If encounters a higher integer, add current trapped water to sum and continue traverse at 1+j.
                i+=j
                sum+=temp
        return sum
