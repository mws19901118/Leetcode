class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        n=len(S)
        S.sort()                                #Sort the list first.
        result=[]
        for i in range(2**n):                   #A length n set has 2^n subsets in total. So use bit manipulation.
            ans=[]
            temp=i
            for j in range(n):
                if temp&1==1:                   #If the least significant bit is 1, append S[j] to ans.
                    ans.append(S[j])
                temp=temp>>1                    #Shift right.
            result.append(ans)                  #Append ans to result.
        return result
