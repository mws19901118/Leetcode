class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        while start <= end:                     #Binary search from 0 to n.
            mid = int((start + end) / 2)
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                start = mid + 1
            else:
                end = mid - 1
        return False
