class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for x in nums:                                #Calculate the overall XOR result of nums.
            xor ^= x
        return "{0:b}".format(xor ^ k).count('1')     #Count the one bits in xor ^ k. These are bits that need to be changed.
