class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        b = 0                          #Initialize the number.
        for x in nums:                 #Traverse nums.
            b = (b << 1) | x           #Shift b to left then add x.
            result.append(b % 5 == 0)  #Append if b is divisible by 5 to result.
        return result
