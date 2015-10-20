class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        n=len(nums)
        result=[]
        dq=collections.deque()                  #Suppose the index of current max value in the window is m. The deque stores in dq[0]. It also stores all the indexes i such that i>m and nums[i]<nums[m]. 
        for i in range(n):
            while dq and nums[dq[-1]]<nums[i]:  #Delete all the indexes in the window from behind whose corrsponding element is smaller than nums[i].
                dq.pop()
            dq.append(i)                        #Append i to the deque.
            if dq[0]==i-k:                      #If the previous max value in the window falls out of window now, popleft its index.
                dq.popleft()
            if i>=k-1:                          #If the window size equals k, append the index of current max value in the window to result.
                result.append(nums[dq[0]])
        return result
