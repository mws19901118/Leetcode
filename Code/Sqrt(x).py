class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x==0:                                                      
            return 0
        i=x/2.0                                       #Initial value for Newton iteration.
        while True:
            j=(i+x/i)/2.0                             #Newton iteration.
            if abs(i-j)< 0.000000000005:              #If the difference betwwen two iterations is smaller than the threshold, stop the loop.
                break
            i=j
        return int(j)                                 #Round to integer.
