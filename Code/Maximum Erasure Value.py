class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:    #Basically, this question is asking the largest sum subarray without duplicate value.
        leftSum, prefixSum, result = 0, 0, 0                    #Intialize the prefix sum on the left, the prefix sum so far and result.
        visited = {-1:0}                                        #Store the prefix sum to where current value is last visited.
        for i, x in enumerate(nums):                            #Traverse nums.
            prefixSum += x                                      #Update prefix sum.
            if x in visited:                                    #If x is visited, update leftSum to visited[x] if it's larger, because all value is positive.
                leftSum = max(leftSum, visited[x])
            visited[x] = prefixSum                              #Update visited[x].
            result = max(result, prefixSum - leftSum)           #Update result to prefixSum - leftSum if it's larger.
        return result                                           #Return result.
