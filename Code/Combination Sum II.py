class Solution:
    def backtrack(self, candidates, list, sum, target, ans):
        if sum==target:
            temp=[]
            for i in list:
                temp.append(i)                                              #If temporary sum equals target, copy list to temp.
            ans.append(temp)
        elif sum<target:
            l=len(candidates)
            for i in range(l):
                if i!=0 and candidates[i]==candidates[i-1]:                 #Eliminate duplication.
                    continue
                list.append(candidates[i])
                sum+=candidates[i]
                self.backtrack(candidates[i+1:], list, sum, target, ans)    #Because elements in combination should be non-descending and only appear once, use candidates[i+1:] in the next step.
                list.pop()
                sum-=candidates[i]
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()                                                   #Sort the candidates.
        sum=0                                                               #Record temporary sum.
        list=[]                                                             #Record the possible combination.                                                    
        ans=[]
        self.backtrack(candidates, list, sum, target, ans)                  #Backtrack.
        ans.sort()
        return ans
