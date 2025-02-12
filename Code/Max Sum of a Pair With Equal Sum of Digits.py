class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result = -1                                                          #Initialize result to be -1.
        max_value = defaultdict(lambda: -inf)                                #Store the max value of a sum of digits, by default it is -inf.
        for x in nums:                                                       #Traverse nums.
            digits_sum = sum(int(y) for y in str(x))                         #Calculate sum of digits.
            result = max(result, max_value[digits_sum] + x)                  #Calculate the pair sum of current value and the max value of current sum of digits; then update result.
            max_value[digits_sum] = max(max_value[digits_sum], x)            #Update the max value of current sum of digits.
        return result
