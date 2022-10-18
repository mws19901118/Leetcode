class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:                                              #If n == 1, directly return "1".
            return "1"
        p = self.countAndSay(n - 1)                             #Get the result of n - 1.
        result, i = "", 0                                       #Initialize result and pointer.
        while i < len(p):                                       #Traverse p.
            j = i + 1
            while j < len(p) and p[j] == p[i]:                  #Count current digit.
                j += 1
            result += str(j - i) + p[i]                         #Add count and the digit to result
            i = j
        return result                                           #Return result.
