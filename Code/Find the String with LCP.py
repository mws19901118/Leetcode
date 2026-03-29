class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)                                                                                                  #Get the dimension.
        if any(lcp[i][i] != n - i for i in range(n)):                                                                 #Validate the lcp on the diagonal, since it is the lcp of 2 identical string so the value should be the length of rest string.
            return ""
        if any(any(lcp[i][j] != lcp[j][i] or lcp[i][j] > n - j for j in range(i + 1, n)) for i in range(n - 1)):      #Traverse the half above diagonal and validate the value should equal to the value at diagonally symmetrical position and not greater than the length of rest string.
            return ""
        s = []                                                                                                        #Initialize result list.
        for i in range(n):                                                                                            #Traverse n to construct s.
            used = [False] * 26                                                                                       #Store if any letter is used that current position cannot use.
            for j in range(i):                                                                                        #Traverse from 0 to i - 1.
                if not lcp[j][i]:                                                                                     #If lcp[j][i] is 0, s[j] is used.
                    used[ord(s[j]) - ord('a')] = True
            if False not in used:                                                                                     #If all letters are used, return "" as not letter can be assigned to current position.
                return ""
            s.append(chr(ord('a') + used.index(False)))                                                               #Find the smallest unused character and append it to s.
        for i in range(n - 1):                                                                                        #Traverse the half above diagonal and validate the 
            for j in range(i + 1, n):
                if s[i] != s[j] and lcp[i][j]:                                                                        #If s[i] != s[j] but lcp[i][j] is greater than 0, s is invalid, return "".
                    return ""
                elif s[i] == s[j] and lcp[i][j] != 1 + (0 if j == n - 1 else lcp[i + 1][j + 1]):                      #If s[i] == s[j] but lcp[i][j] is not equal to 1(j is the end) or 1 + lc[[i + 1][j + 1](j is not the end), s is invalid, return "".
                    return ""
        return "".join(s)                                                                                             #Join s and return.
