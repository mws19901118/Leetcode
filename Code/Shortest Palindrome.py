class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        r = s[::-1]                               #Reverse the string.
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):               #If s starts with r[i:], there is a palindrome, and it's the longest one inside s starting with the first character of s.
                return(r[:i] + s)                 #Form a palindrome according to the problem description and return it.
