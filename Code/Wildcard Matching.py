class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p:                                   #If p is "", return false, unless s is "" too.
            return not s
        m=len(s)
        n=len(p)
        i=0                                         #Record the number of consecutive matching characters starting from the beginning in s.
        j=0                                         #Record the number of consecutive matching characters starting from the beginning in p.
        lastx = 0                                   #Record the last index where '*' appears in s.
        lasty = -1                                  #Record the last index where '*' appears in p.
        while i<m:
            if j<n and (p[j]=='?' or p[j]==s[i]):   #If p[j] equals s[i] or p[j] is '?', go on.
                i+=1
                j+=1
            elif j<n and p[j]=='*':                 #If p[j] is '*', save current indexes.
                lastx=i
                lasty=j
                j+=1
            elif lasty>=0:                          #If there is a '*', if any part is the right of s matches the part behind '*' in p, then s matches p.
                i=lastx+1
                lastx+=1
                j=lasty
            else:
                return False

        if i<m:                                     #If i<m, all the characters in p are matched but there are still remaining characters in s, so s unmatches p.
            return False

        while j<n and p[j]=='*':                    #To deal with If tail '*' in p, j+=1.
            j+=1
        return j==n                                 #If j equals n, s matches p; else, s unmatches p.
