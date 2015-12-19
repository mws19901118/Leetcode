# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:                  #Binary search for the first bad version.
            mid = (start + end) / 2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid + 1
        return start
