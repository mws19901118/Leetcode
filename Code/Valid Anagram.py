class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):      #Count word frequencies.
        if len(s)!=len(t):
            return False
        ds={}
        dt={}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]]=1
            else:
                ds[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in dt:
                dt[t[i]]=1
            else:
                dt[t[i]]+=1
        return ds==dt
