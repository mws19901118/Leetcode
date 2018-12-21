class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [c for c in S if c.isalpha()]     #Find all letters in S and put them in a list in order.
        ans = []
        for c in S:
            if c.isalpha():                         #For each letter in S, append the reverse letter to ans.
                ans.append(letters.pop())
            else:                                   #For each non-letter in S, append it to ans.
                ans.append(c)
        return "".join(ans)                         #Join ans and return.
