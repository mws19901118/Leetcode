class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):                                      #This is a loopy dynamic programming problem.
        l=len(nums)
        if l==0:
            return 0
        elif l==1:
            return nums[0]
        maxp=0
        for j in range(l):                                    #To convert the loopy problem to linear problem, enumerate every starting point, i.e. the house we begin robbing and must rob.
            rob=[[0,0] for i in range(l)]
            rob[0][1]=nums[j]                                 #rob[i][0] means the current max robbed money without robbing house i; while rob[i][1] means the current max robbed money robbing house i.
            rob[0][0]=-0xffffffff                             #Since we must rob this house, set the current max robbed money without robbing house this house as negative infinity.
            for i in range(1,l):
                rob[i][0]=max(rob[i-1][0],rob[i-1][1])
                rob[i][1]=rob[i-1][0]+nums[(j+i)%l]
            maxp=max(rob[l-1][0],maxp)                        #Update the max money robbed. (Because we robbed the first house, we can not rob the last house.)
        return maxp
