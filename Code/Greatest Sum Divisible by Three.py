class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)                                                                              #Calculate sum.
        leastRemain1, secondLeastRemain1, leastRemain2, secondLeastRemain2 = inf, inf, inf, inf    #Initialize the top 2 smallest number whose remainder is 1 or 2 when divided by 3 respectively.
        for x in nums:                                                                             #Traverse nums.
            if x % 3 == 1:                                                                         #If x % 3 == 1, update leastRemain1 and secondLeastRemain1 if necessary.
                if leastRemain1 > x:
                    secondLeastRemain1 = leastRemain1
                    leastRemain1 = x
                elif secondLeastRemain1 > x:
                    secondLeastRemain1 = x
            elif x % 3 == 2:                                                                       #If x % 3 == 2, update leastRemain2 and secondLeastRemain2 if necessary.
                if leastRemain2 > x:
                    secondLeastRemain2 = leastRemain2
                    leastRemain2 = x
                elif secondLeastRemain2 > x:
                    secondLeastRemain2 = x
        if s % 3 == 1:                                                                             #If s % 3 == 1, we can either remove leastRemain1 from s or remove leastRemain2 and secondLeastRemain2 to make s divisible by 3, so return the larger result of them.
            return max(s - leastRemain1, s - leastRemain2 - secondLeastRemain2)
        elif s % 3 == 2:                                                                           #If s % 3 == 2, we can either remove leastRemain2 from s or remove leastRemain1 and secondLeastRemain1 to make s divisible by 3, so return the larger result of them.
            return max(s - leastRemain2, s - leastRemain1 - secondLeastRemain1)
        else:                                                                                      #If s is already divisible by 3, just return it.
            return s
