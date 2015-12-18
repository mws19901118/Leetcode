class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        for x in s:
            if x not in dict:               #Count the number of appearance of each character.
                dict[x] = 1
            else:
                dict[x] += 1
        count = 0
        for x in dict.keys():
            if dict[x] % 2 == 1:
                count += 1
        return count <= 1                   #If there are more than 1 character occurs an odd number of times, return false; otherwise, return true.
