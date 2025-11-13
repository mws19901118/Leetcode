class Solution:
    def maxOperations(self, s: str) -> int:
        result, count, i = 0, 0, 0                  #Initialize result, count of 1 and pointer to traverse.
        while i < len(s):                           #Traverse s.
            if s[i] == '0':                         #If s[i] is '0', move to next.
                i += 1
                continue
            j = i
            while j < len(s) and s[j] == s[i]:      #Find the max j such that s[i:j] only contains '1'.
                j += 1
            if j < len(s):                          #If j is not the end, s[j] is 0.
                count += j - i                      #Update count.
                result += count                     #We can move all 1 to the right.
            i = j                                   #Move i to j.
        return result
