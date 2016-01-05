class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currentsum = 0                                                  #Record the sum from beginning to current index.
        dict = {0:-1}                                                   #Record the first occurrence of certain value of currentsum. The initial currentsum is 0, and its index is -1.
        maxlength = 0
        for i in range(len(nums)):
            currentsum += nums[i]                                       #Calculate current sum by adding number in current index.
            if currentsum - k in dict:                                  #If currentsum - k is in dict, there is at least 1 subarray whose sum is k, so find the maxlength.
                maxlength = max(maxlength, i - dict[currentsum - k])
            if currentsum not in dict:                                  #Add the index for currentsum to dict if currentsum is not in dict already.
                dict[currentsum] = i
        return maxlength
