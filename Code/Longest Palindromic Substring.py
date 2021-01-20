class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0                                                                   #Record the starting index of current longest palindromic substring.
        l = 1                                                                       #Record the length of current longest palindromic substring.
        i = 0                                                                       #Traverse every "core" of palindromic substring. "Core" means a sequence of same characters which could be in the exact middle of a palindromic substring. 
        while i < len(s) - l // 2:                                                  #The starting index of the last possible "core" is n-l/2.
            left, right = i, i                                                      #Record the left and right boundry of palindromic substring.
            while right < len(s) - 1 and s[right] == s[right + 1]:                  #Determine the right boundry of "core".
                right += 1
            i = right + 1                                                           #Set the starting point of next "core".
            while right < len(s) - 1 and left > 0 and s[left - 1] == s[right + 1]:  #Traverse to both directions to determine the left boundry and right boundry.
                left -= 1
                right += 1
            if right - left + 1 > l:                                                #Update l and start if necessary.
                l = right - left + 1
                start = left
        return s[start:start + l]
