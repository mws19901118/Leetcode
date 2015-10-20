class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n=len(s)
        if n<=1:                                                    #If the length of s is smaller than or equal to 1, it's palindromic.
            return s
        start=0                                                     #Record the starting index of current longest palindromic substring.
        l=1                                                         #Record the length of current longest palindromic substring.
        i=0                                                         #Traverse every "core" of palindromic substring. "Core" means a sequence of same characters which could be in the exact middle of a palindromic substring. 
        while i<n-l/2:                                              #The starting index of the last possible "core" is n-l/2.
            left=i                                                  #Record the left boundry of palindromic substring.
            right=i                                                 #Record the right boundry of palindromic substring.
            while right<n-1 and s[right]==s[right+1]:               #Determine the right boundry of "core".
                right+=1
            i=right+1                                               #Set the starting point of next "core".
            while right<n-1 and left>0 and s[left-1]==s[right+1]:   #Traverse to both directions to determine the left boundry and right boundry.
                left-=1
                right+=1
            if right-left+1>l:                                      #Update l and start if necessary.
                l=right-left+1
                start=left
        return s[start:start+l]
