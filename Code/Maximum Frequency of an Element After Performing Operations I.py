class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = max(nums)                                                           #Get the max number.
        count = [0] * (n + 1)                                                   #Counting sort nums.
        for num in nums:
            count[num] += 1
        prefixSum = [0]                                                         #Build the prefix sum of count at each value.
        for i in range(n + 1):
            prefixSum.append(prefixSum[-1] + count[i])
        result = 0
        for i in range(n + 1):                                                  #Traverse from 0 to n.
            left = prefixSum[i] - prefixSum[max(0, i - k)]                      #Find the total numbers in the range max(0, i - k) to i - 1.
            right = prefixSum[min(n + 1, i + k + 1)] - prefixSum[i + 1]         #Find the total numbers in the range of i + 1 to min(i + k, n).
            result = max(result, count[i] + min(numOperations, left + right))   #Since the operation has a limit, we can update at most min(numOperations, left + right) numbers to i. Thus update result if count[i] + min(numOperations, left + right) is larger.
        return result
