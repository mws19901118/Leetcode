class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        xor = 0
        for x in nums:                            #Suppose the single numbers are a and b, calculate a ^ b by xor the whole array because numbers not a or b will be consolidated.
            xor ^= x
        rightMost = xor & (-xor)                  #Find the rightmost bit in a ^ b, which is the right most bit diff of a and b.
        a = 0                                     #Initialize a.
        for x in nums:                            #Traverse nums.
            if x & rightMost:                     #If current number has bit on rightMost, it could be a candidate of a, so a to xor with current number.
                a ^= x
        return [a, xor ^ a]                       #Now a is found, return a and xor ^ a, which is b.
