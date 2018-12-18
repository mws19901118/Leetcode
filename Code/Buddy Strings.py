from collections import defaultdict

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A is None or B is None or len(A) != len(B):                                        #The length of A and B must be equal.
            return False
        if A == B:                                                                            #If A and B are same, the string must contain a character which appears more than once.
            map = defaultdict(int)
            for c in A:
                if map[c] > 0:
                    return True
                else:
                    map[c] += 1
            return False
        else:
            length = len(A)
            start = 0                                                                         #Find the first index where A differs with B.
            while start < length and A[start] == B[start]:
                start += 1
            end = length - 1                                                                  #Find the last index where A differs with B.
            while end >= 0 and A[end] == B[end]:
                end -= 1
            return start != end and A[end] + A[start + 1:end] + A[start] == B[start:end + 1]  #If the first index and last index are same, there are only one different character, so it does not fit the requirement of Buddy Strings.
                                                                                              #Swap the first difference and last difference in A, and check if the string after swap equals to B, leaving out the same prefix and suffix.
