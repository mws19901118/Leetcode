class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        l=len(num)
        if l==0:
            return 0
        rob=[[0,0] for i in range(l)]                 #Initialize the rob array to record the current max money robbed.
        rob[0][1]=num[0]                              #rob[i][0] means the current max robbed money without robbing house i; while rob[i][1] means the current max robbed money robbing house i. 
        for i in range(1,l):
            rob[i][0]=max(rob[i-1][0],rob[i-1][1])
            rob[i][1]=rob[i-1][0]+num[i]
        return max(rob[l-1][0],rob[l-1][1])           #Return the greater value of rob[l-1][0] and rob[l-1][1]
