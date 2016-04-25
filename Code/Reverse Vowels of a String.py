class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = list(s)                                                   #Convert string to list of characters.
        start = 0
        end = len(s) - 1
        while start < end:                                            #Use 2 pointers to go through from 2 sides to middle.
            if c[start] in 'aeiouAEIOU' and c[end] in 'aeiouAEIOU':   #If characters on start and end are both vowels, swap them, then increase start by 1 and decrease end by 1.
                c[start], c[end] = c[end], c[start]
                start += 1
                end -= 1
            while start < end and c[start] not in 'aeiouAEIOU':       #If characters on start is not vowel, increase start by 1.
                start += 1
            while start < end and c[end] not in 'aeiouAEIOU':         #If characters on end is not vowel, decrease end by 1.
                end -= 1
        return ''.join(c)                                             #Join the characters and return it.
