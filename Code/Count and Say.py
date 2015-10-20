class Solution:
    def generate(self, s):
        if s=="":
            return "1"
        l=len(s)
        i=0
        ans=""
        while i<l:
            j=1
            while i+j<l and s[i+j]==s[i]:       #Count the number of consecutive same digits.
                j+=1
            ans+=str(j)+s[i]                    #Append to result.
            i+=j
        return ans
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n==0:                                #If n==0, return "".
            return ""
        
        ans=""
        for i in xrange(n):                     #Generate sequence basing on the last sequence n times.
            ans=self.generate(ans)
        return ans
