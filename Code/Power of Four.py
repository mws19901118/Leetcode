class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:                #0 is not power of 4.
            return False
        while num != 1:             #While num is not 1, if num can not be divided by 4, it's not power of 4.
            if num % 4 != 0:
                return False
            num >>= 2               #Right shift num by 2.
        return True                 #Return true.
