class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()                                   #Sort the list.
        result=0x7fffffff                             #Set the initial value of result to be a very large value.
        for i in range(len(nums)-2):                  #Enumerate the first smallest integer i of the 3 integers.
            j=i+1                                     #Set the second integer j to be the integer behind i.
            k=len(nums)-1                             #Set the third integer k to be the last element in the list.
            while j<k:                                #Ensure j is smaller than or equal to k.
                t=nums[i]+nums[j]+nums[k]             #This is the temporary sum t=i+j+k.
                if t==target:                         #If t equals target, it's the closest sum, return it.
                    return t
                if abs(t-target)<abs(result-target):  #If the distance between t and target is smaller than the distance between result and target, update result with t.
                    result=t
                if t<target:                          #If t is smaller than target, replace j with the next integer to increase temporary sum.
                    j+=1
                else:                                 #If t is greater than target, replace k with the previous integer to decrease temporary sum.
                    k-=1
        return result
