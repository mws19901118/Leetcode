class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)                                            #Count nums.
        result = 0
        for x in count:                                                  #Traverse count.
            if count[x] > 0 and count[x + 1] > 0:                        #If both count[x] and count[x + 1] is greater than 0, the subsequence formed by all occurrences of x and all occurrences of x + 1 is harmonious. 
                result = max(result, count[x] + count[x + 1])            #Update result if necessary.
        return result
