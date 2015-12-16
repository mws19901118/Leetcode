class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if l < 2:
            return []
        t = 0
        for x in nums:
            t ^= x                                #Find the xor of the 2 single numbers.
        bits = 0
        while (t >> bits) % 2 == 0:
            bits += 1                             #Find the lowest bit where they are different.
        t0 = 0
        t1 = 0
        for x in nums:
            if (x >> bits) % 2 == 0:              #According to the value at this bit, divide the original numbers into 2 groups, each of which has only 1 single number. Find the single number using xor operation respectively.
                t0 ^= x
            else:
                t1 ^= x
        return [t0, t1]
