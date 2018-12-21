from fractions import gcd
from functools import reduce
from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        return reduce(gcd, Counter(deck).values()) >= 2   #Find the greatest common divisor of counts of each number. 
                                                          #Return if the gcd is larger than or equal to 2.
