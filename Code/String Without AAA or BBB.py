class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        s = ""
        while A > B and B > 0:                #While A > B > 0, append "aab" to s and maintain A and B.
            s += "aab"
            A -= 2
            B -= 1
        while B > A and A > 0:                #While B > A > 0, append "bba" to s and maintain A and B. This case and the above case won't happen at the same time.
            s += "bba"
            B -= 2
            A -= 1
        if A == B:                            #If A == B, append the remaining characters in the format of "ab" if s is empty or the last character is "b".
            if len(s) == 0 or s[-1] == 'b':
                for i in range(A):
                    s += "ab"
            else:                             #Otherwise, append the remaining characters in the format of "ba".
                for i in range(A):
                    s += "ba"
        else:                                 #If A != B, then either A or B is 0. Append the remaining "a" or "b" to s.
            for i in range(A):
                s += "a"
            for i in range(B):
                s += "b"
        return s
