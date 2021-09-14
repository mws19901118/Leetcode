class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]     #Find all letters in s and put them in a list in order.
        ans = []
        for c in s:
            if c.isalpha():                         #For each letter in s, append the reverse letter to ans.
                ans.append(letters.pop())
            else:                                   #For each non-letter in s, append it to ans.
                ans.append(c)
        return "".join(ans)                         #Join ans and return.
