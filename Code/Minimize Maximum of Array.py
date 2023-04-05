class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cumulativeSum = 0                                             #Store the cumulative sum from beginning.
        result = 0                                                    #Initialize result.
        for i, x in enumerate(nums):                                  #Traverse nums.
            if x - result > result * i - cumulativeSum:               #If the delta from result result to x can fill all the gaps from each number to result before x and there is still more, update result.
                result = ceil((cumulativeSum + x) / (i + 1))          #The new min max is the ceiling of cumulative sum so far divided by total number.
            cumulativeSum += x                                        #Update cumulative sum.
        return result                                                 #Return result.
