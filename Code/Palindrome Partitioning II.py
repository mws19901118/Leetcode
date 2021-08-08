class Solution:
    def minCut(self, s: str) -> int:
        isPalindrome = [[False for _ in range(len(s))] for _ in range(len(s))]                  #Initialize 2D array where isPalindrome[i][j] indicating whether s[i:j + 1] forms a palindrome. 
        cut = [len(s)] * len(s)                                                                 #Cut[i] means the min cut for s[i:]
        for i in reversed(range(len(s))):                                                       #Traverse backward.
            for j in range(i, len(s)):                                                          #Traverse from s[i] to the end of s.
                if s[i] == s[j] and (j - i < 2 or isPalindrome[i + 1][j - 1]):                  #If s[i] == s[j] and s[i + 1:j] is a palindrome or the length of s[i:j + 1] less than 2, s[i:j + 1] forms a palindrome.
                    isPalindrome[i][j] = True
                    cut[i] = 0 if j == len(s) - 1 else min(cut[i], cut[j + 1] + 1)              #If j == len(s) - 1, the string s[i:] is a palindrome, cut[i] = 0; otherwise update cut[i] to be cut[j] + 1 if the latter one is smaller.
        return cut[0]                                                                           #Return min cut for s.
