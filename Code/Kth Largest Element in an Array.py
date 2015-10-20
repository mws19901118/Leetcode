class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):    
        if k==1:                                                #When k is 1, just return the maximum value of nums to avoid dead loop.
            return max(nums)
        l=len(nums)
        mid=nums[l/2]                                           #Let mid be the middle element of nums.
        low=[]
        high=[]
        for i in range(l):
            if i!=l/2:
                if nums[i]<=mid:
                    low.append(nums[i])                         #Append all the element which is smaller than or equal to mid except for mid to low
                else:
                    high.append(nums[i])                        #Append all the element which is larger than mid to high.
        high.append(mid)                                        #Append mid to high.
        if len(high)==k:                                        #If length of high is equal to k, then mid is the kth largest number in nums.
            return mid
        elif len(high)>k:                                       #If length of high is larger than k, the kth largest number is in high.
            return self.findKthLargest(high, k)
        else:
            return self.findKthLargest(low, k-len(high))        #If length of high is smaller than k, high contains the first len(high) largest number and we should find the (k-len(high))th largest number in low.
