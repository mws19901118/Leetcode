# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:                 #Binary search from 1 to n.
            mid = (start + end) // 2
            result = guess(mid)
            if not result:
                return mid
            elif result < 0:
                end = mid - 1
            else:
                start = mid + 1
