class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0     #If the number of stones can be divided by 4, you will always lose, because you can only take at most 3 stones once, your opponent will can always make the sum of each round to 4.
                              #Otherwise, you can always win by make the number of stones be divided by 4 after you take the stone first time.
