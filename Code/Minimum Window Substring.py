from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if m < n or n == 0:                         #If s is shorter than t or t is empty string, return ''.
            return ''
        d = Counter(t)                              #Count the characters in t.
        minl = m + 1                                #Maintain the min length of window.
        result = ''                                 #Store the result.
        count = 0                                   #Count how many unique characters whose counts are matched of t are found in the window
        i = 0                                       #Two pointers: i indicates the end of window and j in indicates the start of window.
        j = 0
        dict= {}                                    #Count the characters of t in the window, initially 0.
        for x in d:
            dict[x] = 0
        while i < m:                                #While haven't reached the end of s, maintain dict as follows.
            while i < m and count < len(d):         #Move i forward while haven't matched all characters.
                if s[i] in d:
                    dict[s[i]] += 1                 #Maintain dict.
                    if dict[s[i]] == d[s[i]]:       #If match a characters, update count.
                        count += 1
                i += 1
            if count == len(d):                     #If match all characters, update minl and result.
                if minl > i - j:
                    minl = i - j
                    result = s[j:i]
            while j < i and count == len(d):        #Move j forward j is smaller than i and have matched all characters.
                if s[j] in d:
                    dict[s[j]] -= 1                 #Maintain dict.
                    if dict[s[j]] < d[s[j]]:        #If unmatch a characters, update count.
                        count -= 1
                j += 1
            if count < len(d):                      #If can not match all characters, update minl and result.
                if minl > i - j + 1:
                    minl = i - j + 1
                    result = s[j - 1:i]
        if minl == m + 1:                           #If can npt find such window, return ''.
            return ""
        else:                                       #Otherwise, return result.
            return result
