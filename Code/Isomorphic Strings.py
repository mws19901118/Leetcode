class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ss=[]                               #Store the index of first apperence of each character of s.
        tt=[]                               #Store the index of first apperence of each character of t.
        ls=len(s)
        lt=len(t)
        if ls!=lt:
            return False
        for i in range(ls):
            j=0
            while j<i:
                if s[ss[j]]==s[i]:
                    break
                j+=1
            ss.append(j)
        for i in range(lt):
            j=0
            while j<i:
                if t[tt[j]]==t[i]:
                    break
                j+=1
            tt.append(j)
        if ss==tt:
            return True
        else:
            return False
