from collections import defaultdict
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = set()                                 #Create a set to count groups.
        for s in A:
            odd = []
            even = []
            for i in range(len(s)):
                if i % 2:                             #Get all the characters in odd index.
                    odd.append(s[i])
                else:                                 #Get all the characters in even index.
                    even.append(s[i])
            odd.sort()                                #Sort odd to get the unique composition of odd.
            even.sort()                               #Sort even to get the unique composition of even.
            group.add(("".join(odd), "".join(even)))  #Join odd and even to string respectively and put them into a tuple then put the tuple in set.
        return len(group)
