class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        n=len(s)
        result=[]
        i=1
        while i<=3:                                         #First delimiter
            j=i+1
            while j<=i+3 and j<n:                           #Second delimiter
                k=j+1
                while k<=j+3 and k<n:                       #Third delimiter
                    t1=int(s[:i])                           #Four parts of IP
                    t2=int(s[i:j])
                    t3=int(s[j:k])
                    t4=int(s[k:])
                    if (t1>=0 and t1<=255) and (t2>=0 and t2<=255) and (t3>=0 and t3<=255) and (t4>=0 and t4<=255):     #Check validity.
                        ans=str(t1)+'.'+str(t2)+'.'+str(t3)+'.'+str(t4)
                        if result.count(ans)==0 and len(ans)==n+3:                      #Length should equal original length plus 3 delimiters.
                            result.append(ans)
                    k+=1
                j+=1
            i+=1
        return result
