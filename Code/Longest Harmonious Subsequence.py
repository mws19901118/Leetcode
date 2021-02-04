class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter()                                   #Use a counter to store count of each element.
        result = 0                                      #Initialize result to be 0.
        for x in nums:                                  #Traverse nums.
            c[x] += 1                                   #Increase count of x.
            if c[x - 1]:                                #If c[x - 1] > 0, update result to c[x] + c[x - 1] if it's greater than result.
                result = max(c[x] + c[x - 1], result)
            if c[x + 1]:                                #If c[x + 1] > 0, update result to c[x] + c[x + 1] if it's greater than result.
                result = max(c[x] + c[x + 1], result)
        return result
