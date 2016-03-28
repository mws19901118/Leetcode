class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        dict = {}                                     #Maintain a dictionary whose length is at most k. (Could be optimized using LRU cache.)
        last = -1                                     #Record the index before current window starts.
        maxl = 0                                      #Record the max length of window.
        for i in range(len(s)):
            if s[i] not in dict and len(dict) == k:   #If there are already k characters in dict, find the character with the smallest index then remove it from dict.
                minindex = i
                c = ''
                for x in dict:
                    if dict[x] < minindex:
                        minindex = dict[x]
                        c = x
                del dict[c]
                last = minindex                       #Update last.
            dict[s[i]] = i                            #Update the most recent index of current character.
            maxl = max(i - last, maxl)                #Update maxl
        return maxl
