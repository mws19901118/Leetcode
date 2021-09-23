class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:                                                            #If palindrome length is 1, cannot break it, so return "".
            return ""
        firstIndexNotA = -1
        for i in range(len(palindrome) // 2):                                               #Traverse the first half of palindrome and find the index of first lettre that is not 'a'.
            if palindrome[i] != 'a':
                firstIndexNotA = i
                break
        result = ""                                                                         #Initialize result.
        if firstIndexNotA >= 0:                                                             #If there is such index, replace the character at index with 'a' and return.
            return palindrome[:firstIndexNotA] + 'a' + palindrome[firstIndexNotA + 1:]
        else:                                                                               #Otherwise, replace last character with 'b' and return.
            return palindrome[:-1] + 'b'
