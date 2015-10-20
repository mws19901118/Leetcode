class Solution:
    def backtrack(self, start, list, sum, target, k, ans):
        if sum==target:
            if len(list)==k:
                temp=[]
                for i in list:
                    temp.append(i)                                #If temporary sum equals target and temporary length equals k, copy list to temp.
                ans.append(temp)
        elif sum<target:
            for i in range(start+1,10):                           #Traverse from start+1 to 10.
                list.append(i)
                sum+=i
                self.backtrack(i, list, sum, target,k, ans)       #Because elements in combination should be ascending, use i as the start number in the next step.
                list.pop()
                sum-=i
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        sum=0                                                     #Record temporary sum.
        list=[]                                                   #Record the possible combination.
        ans=[]
        self.backtrack(0, list, sum, n, k, ans)                   #Backtrack.
        return ans
