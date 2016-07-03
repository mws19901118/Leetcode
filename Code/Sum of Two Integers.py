import ctypes
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sum = 0
        carry = ctypes.c_int32(b)                           #Set b as the carry.
        while carry.value != 0:                             #While carry is not 0, keep add current sum and carry.
            sum = a ^ carry.value                           #Get the sum of each bit by XOR.
            carry = ctypes.c_int32((a & carry.value) << 1)  #Use AND to get new carry for each bit and shift it left 1 bit.
            a = sum
        return sum
