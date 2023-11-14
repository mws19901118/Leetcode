class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0                                        #Initialize count.
        for x in set(s):                                 #Traverse the distinct characters in s.
            left, right = s.find(x), s.rfind(x)          #Find the first and last apperance of x in s.
            count += len(set(s[left + 1:right]))         #The number of distinct characters between left and right(not inclusive) is the number of length-3 palindrome whose 2 ends are x.
        return count
