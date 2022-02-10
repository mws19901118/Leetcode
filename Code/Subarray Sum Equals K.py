class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)               #Count the appearances of prefix sum value.
        prefixSums[0] = 1                           #Initially, it's 0.
        for x in nums:                              #Traverse the list.
            s += x                                  #Calculate current prefix sum value.
            count += prefixSums[s - k]              #Add the count of prefix sum whose value is s - k to result. The subarray starting after prefix sum s - k ending at current element has a sum equals k.
            prefixSums[s] += 1                      #Update the count of current prefix sum value.
        return count
