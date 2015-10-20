class Solution:
    def backtrack(self, list, nums, flag, tlen, length, ans):
        if tlen==length:
            temp=[]
            for i in list:
                temp.append(i)                                              #If temporary length equals length of nums, copy list to temp.
            ans.append(temp)
        else:
            l=len(nums)
            for i in range(l):
                if flag[i]==False:
                    list.append(nums[i])
                    tlen+=1
                    flag[i]=True
                    self.backtrack(list, nums, flag, tlen, length, ans)
                    list.pop()
                    tlen-=1
                    flag[i]=False
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        flag=[False]*len(nums)                                              #Record if current element is already taken by permulation.
        list=[]
        ans=[]                                                              #Record the possible combination.
        self.backtrack(list, nums, flag, 0, len(nums), ans)                 #Backtrack.
        return ans
