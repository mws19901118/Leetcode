class Solution(object):
   def singleNumber(self, nums: List[int]) -> List[int]:
        t = 0
        for x in nums:                              #Find the xor of the 2 single numbers.
            t ^= x
        bits = 0
        while t & 1 == 0:                           #Find the lowest bit where they are different.
            t >>= 1
            bits += 1
        t0, t1 = 0, 0                               #According to the value at this bit, divide the original numbers into 2 groups, each of which has only 1 single number. Find the single number using xor operation respectively.
        for x in nums:
            if (x >> bits) & 1:
                t0 ^= x
            else:
                t1 ^= x
        return [t0, t1]
