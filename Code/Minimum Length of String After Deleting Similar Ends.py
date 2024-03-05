class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1                          #Initialize 2 pointers at the beginning of s and end of s.
        while i < j and s[i] == s[j]:                 #Traverse both pointers towards the middle until they meet or the characters on 2 pointers don't match.
            k = i + 1
            while k <= j and s[k] == s[i]:            #Move i forward until it is not equal to the current s[i].
                k += 1
            i = k
            k = j - 1
            while i <= k and s[k] == s[j]:            #Move j backward until it is not equal to the current s[j].
                k -= 1
            j = k
        return max(0, j - i + 1)                      #Return the max of length of [s[i:j + 1] and 0.
