class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:                  #Rule out 0.
            return False
        while num % 2 == 0:           #Divided it by 2 as many times as it can.
            num /= 2
        while num % 3 == 0:           #Divided it by 3 as many times as it can.
            num /= 3
        while num % 5 == 0:           #Divided it by 5 as many times as it can.
            num /= 5
        if num == 1:                  #If the result is 1, it's an ugly number; otherwise, it's not.
            return True
        else:
            return False
