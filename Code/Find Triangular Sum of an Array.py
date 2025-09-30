class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0                                                              #Initialize result.
        combination = 1                                                         #Initialize combination to be 1, comb(len(nums) - 1, 0).
        for i, x in enumerate(nums):                                            #Traverse nums.
            result = (result + combination * x) % 10                            #The contribution of each number towards final triangular sum is its combination, so add combination * x to result and take the last digit.
            combination = combination * (len(nums) - 1 - i) // (i + 1)          #Calculate next combination.
        return result
