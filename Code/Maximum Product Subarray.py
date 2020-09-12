class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:                                                                      #If nums is empty, return 0.
            return 0
        maxp, minp = [nums[0]], [nums[0]]                                                   #Initialize the max product list and min product list with the 1st number in nums.
        for i in range(1, len(nums)):                                                       #Iterate through nums from the 2nd number.
            maxp.append(max(nums[i], maxp[i - 1] * nums[i], minp[i - 1] * nums[i]))         #Find the max product ending at current number.
            minp.append(min(nums[i] ,maxp[i - 1] * nums[i], minp[i - 1] * nums[i]))         #Find the min product ending at current number.
        return max(maxp)                                                                    #Return the max value in maxp.
