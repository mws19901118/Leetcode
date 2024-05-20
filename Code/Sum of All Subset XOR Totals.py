class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0                                          #Initialize result.
        for x in nums:                                      #Traverse nums.
            result |= x                                     #Result OR with current number.
        return result << (len(nums) - 1)                    #Shift len(nums) - 1 bits left and return.
                                                            #Suppose there are n numbers, so there are 2 ^ n subsets and each number will appear in 2 ^ (n - 1) subsets.
                                                            #For any bit to be set in any subset XOR total, it must be set in an odd number of the elements in the subset.
                                                            #And for any bit is set in at least one of the numbers, it will appear in half of the XOR totals, which can be proved by induction starting at 0, 1 and etc.
                                                            #So, we calculate the OR total for all numbers and all the bits in it will appear in 2 ^ (n - 1) subsets.
                                                            #Thus shift n - 1 bits left.
