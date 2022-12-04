class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        firstSum, lastSum = 0, sum(nums)                                                                                      #Initialize first sum and last sum to be 0 and sum of nums.
        minAverageDifference, index = float('inf'), -1                                                                        #Initialize minimum average difference to be a really large number and index to be -1.
        for i, x in enumerate(nums):                                                                                          #Traverse nums.
            firstSum += x                                                                                                     #Add current number to firstSum.
            lastSum -= x                                                                                                      #Substract current number from lastSum.
            averageDifference = abs(firstSum // (i + 1) - ((lastSum // (len(nums) - i - 1)) if i < len(nums) - 1 else 0))     #Calculate current average difference, be aware of the special case when i reaches end, last average should be 0.
            if averageDifference < minAverageDifference:                                                                      #Update minAverageDifference and index if necessary.
                minAverageDifference = averageDifference
                index = i
        return index                                                                                                          #Return index.
        
