class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:                                                            #If palindrome length is 1, cannot break it, so return "".
            return ""
        for i in range(len(palindrome) // 2):                                               #Traverse the first half of palindrome and find the index of first lettre that is not 'a'.
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]                            #If there is such index, replace the character at index with 'a' and return.                                                                           
        return palindrome[:-1] + 'b'                                                        #Otherwise, replace last character with 'b' and return.
