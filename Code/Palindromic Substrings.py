class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        left, right = 0, 0                                                                  #Initialize the left center and right center of palindromic substring at the beginning of s.
        while left <= len(s) - 1 and right <= len(s) - 1:                                   #Traverse each possible center of palindromic substring.
            i = 0
            while left - i >= 0 and right + i < len(s) and s[left - i] == s[right + i]:     #Expand palindromic substring by 1 character on each side if possible.
                count += 1
                i += 1
            (left, right) = (left, right + 1) if left == right else (left + 1, right)       #If left center and right center is equal, move right center to next; otherwise move left center to catch right center.
        return count
