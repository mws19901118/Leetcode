class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)                                                #Count each number.
        result, carry = 0, 0                                                 #Initialize result and the total number carried from previous number.
        for i in range(min(count.keys()), max(count.keys()) + 1):            #Traverse from the min value to max value.
            newCarry = max(carry + count[i] - 1, 0)                          #Calculate new carry, only one number can stay current value.
            result += newCarry                                               #Add new carry to result and then replace carry with new carry.
            carry = newCarry
        return result + carry * (carry - 1) // 2                             #If there are carry remain, it needs carry * (carry - 1) // 2 more operations.
