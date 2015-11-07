class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = len(s)
        l2 = len(t)
        if abs(l1 - l2) > 1:                            #If the difference between the lengthes of 2 strings is larger than 1, the edit distance can not be 1.
            return False
        if l1 == l2:                                    #If the 2 lengthes are equal, count the differences of each corresponding characters.
            count = 0
            for i in range(l1):
                if s[i] != t[i]:
                    count += 1
            if count == 1:                              #If the count is 1, return true; otherwise, return false.
                return True
            else:
                return False
        else:                                           #If the 2 lengthes are not equal, let a be the shorter string, b be the longer string.
            if l1 < l2:
                a = s
                b = t
            else:
                a = t
                b = s
            i = 0
            while i < len(a) and a[i] == b[i]:          #Find the index of first difference of character.
                i += 1
            while i < len(a) and a[i] == b[i + 1]:      #If edit distance is 1, beginning with i, a[i] should equals to b[i + 1].
                i += 1
            if j < len(a):
                return False
            else:
                return True
