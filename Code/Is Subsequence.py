    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0                                       #Use 2 pointers to traverse i and j.
        while i < len(s) and j < len(t):
            i += s[i] == t[j]                             #If s[i] equals t[j], increase i by 1.
            j += 1                                        #Always increase j.
        return i == len(s)                                #Return if i reaches the end of s.
