class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result, min_v, max_v, min_diff, max_diff = 0, nums[0], nums[0], inf, -inf      #Initialize result, max value, max value, min diff between pair and max diff between pair.
        for k in range(2, len(nums)):                                                  #Traverse k from 2 to the end of nums.
            min_diff = min(min_diff, min_v - nums[k - 1])                              #Update min diff, i.e. min nums[i] - nums[j].
            max_diff = max(max_diff, max_v - nums[k - 1])                              #Update max diff, i.e. max nums[i] - nums[j].
            min_v = min(min_v, nums[k - 1])                                            #Update min value.
            max_v = max(max_v, nums[k - 1])                                            #Update max value.
            result = max(result, min_diff * nums[k], max_diff * nums[k])               #Update result if any min_diff * nums[k] or max_diff * nums[k] is greater.
        return result
