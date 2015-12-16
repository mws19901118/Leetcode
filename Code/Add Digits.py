class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:                    #If num is 0, return 0.
            return 0
        return 1 + (num - 1) % 9        #Otherwise, return the digital root of num(1 + (num - 1) % 9).
