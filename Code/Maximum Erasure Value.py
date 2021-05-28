class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        indexes = {}                                        #Store the index of each integer.
        leftEnd, currentSum, maxScore = 0, 0, 0             #Initialize the left end of subarray, current subarray sum and max score.
        for i, x in enumerate(nums):                        #Traverse nums.
            if x in indexes:                                #If x is already seen, remove all integers from left end to last index of x from current sum and indexes.
                lastIndex = indexes[x]
                for y in nums[leftEnd:lastIndex + 1]:
                    currentSum -= y
                    del indexes[y]
                leftEnd = lastIndex + 1                     #Update new left end to be the next of last index of x.
            currentSum += x                                 #Add x to current sum.
            maxScore = max(maxScore, currentSum)            #Keep updating max score so far.
            indexes[x] = i                                  #Add current index to map.
        return maxScore
