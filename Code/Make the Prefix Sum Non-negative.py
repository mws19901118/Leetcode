class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        heap = []                                      #Initialize a min heap to store candidates to be moved to the end of list.
        prefix_sum, result = 0, 0                      #Initialize prefix sum and result.
        for x in nums:                                 #Traverse nums.
            if x < 0:                                  #If current number is nagative, it is a candidate to be moved, so push it to heap.
                heapq.heappush(heap, x)
            prefix_sum += x                            #Update prefix sum.
            if prefix_sum < 0:                         #If prefix sum is negative now, pop the smallest candidate from heap and append it to the end of list.
                nums.append(heapq.heappop(heap))
                prefix_sum -= nums[-1]                 #Restore prefix sum.
                result += 1                            #Increase result.
        return result
