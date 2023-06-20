class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)                  #Initialize result array for each number with value -1.
        span = 2 * k + 1                           #Span of sliding window is 2 * k + 1.
        s = sum(nums[:span - 1])                   #Calculate the sum of nums[:span - 1].
        for i in range(k, len(nums) - k):          #Traverse valid indexes in [k, len(nums) - k - 1].
            s += nums[i + k]                       #Add nums[i + k] to s as the sliding window moves in to nums[i + k].
            result[i] = s // span                  #Calculate k radius subarray average and update result[i].
            s -= nums[i - k]                       #Remove nums[i - k] from s as the sliding window moves out of nums[i - k].
        return result
