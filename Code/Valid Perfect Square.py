class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:                        #If num is 1, return true.
            return True
        start = 0
        end = num
        while start + 1 < end:              #Binary search from 0 to num. If it reaches 2 adjacent integers, stop binary search, because mid will always stuck in the middle.
            mid = int((start + end) / 2)
            square = mid * mid              #Calculate mid and square of mid.
            if square == num:               #If square equals num, num is perfact square, return true.
                return True
            elif square < num:
                start = mid
            else:
                end = mid
        return False                        #Return false if binary search finishes.
