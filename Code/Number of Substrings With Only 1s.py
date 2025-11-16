class Solution:
    def numSub(self, s: str) -> int:
        i, count = 0, 0                                                      #Initialize pointer and count.
        division = 10 ** 9 + 7                                               #Initialize division.
        while i < len(s):                                                    #Traverse s.
            j = i
            while j < len(s) and s[j] == s[i]:                               #Find all substrings s[i:j] that only has 1 character.
                j += 1
            if s[i] == '1':                                                  #If the character is 1, there are total (1 + j - i) * (j - i) // 2 substrings.
                count = (count + (1 + j - i) * (j - i) // 2) % division
            i = j                                                            #Move i to j.
        return count
