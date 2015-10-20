class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()                                               #In order that a<=b<=c, sort the list.
        n=len(nums)
        dict={}                                                   #Record the index of first appearance of each value.
        result=[]
        for i in range(n):
            if nums[i] not in dict:
                dict[nums[i]]=i
        for i in range(n-2):                                      #The last possible index of a is n-3.
            if nums[i]>0:                                         #a can't be great than 0.
                break
            if i>0 and nums[i]==nums[i-1]:                        #To rule out duplicates, only consider the first appearance of each value.
                continue
            for j in range(i+1,n-1):                              #The last possible index of a is n-2.
                if nums[j]>-nums[i]:                              #b can't be great than -a.
                    break
                if j>i+1 and nums[j]==nums[j-1]:                  #To rule out duplicates, only consider the first appearance of each value.
                    continue
                c=-nums[i]-nums[j]
                if c in dict:                                     #If c is in dict, there might be a possible solution.
                    if c>nums[j]:                                 #If c>b, it's ok.
                        result.append([nums[i],nums[j],c])
                    elif c==nums[j]:                              #If c=b, only when there are mutipule appearance of b, it's a legal solution.
                        if nums[j+1]==nums[j]:
                            result.append([nums[i],nums[j],c])
        return result
