class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:    #Find the first element i which violate the descending order from i to the end, i.e. nums[i]<nums[i+1].
            i-=1
        if i==-1:                             #If can't find such element, the array is totally descending. Thus, we can't get the next permutation. So we reverse the array to sort it in ascending order.
            nums.reverse()
        else:
            j=n-1
            while nums[j]<=nums[i]:           #Search from the end to i to find the first element j which is greater than i.
                j-=1
            a=nums[i]                         #Swap the value of nums[i] and nums[j]. That's the beginning of difference between current permutation and next permutation.
            nums[i]=nums[j]
            nums[j]=a
            t=nums[i+1:]                      #Reverse the array behind i to sort it in ascending order
            t.reverse()
            nums[i+1:]=t
