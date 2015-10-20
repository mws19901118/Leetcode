class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):                                              #This is a dynamic programming problem.
        n=len(s)
        A=[[False for a in range(n)] for b in range(n)]               #A[i][j] means whether s[i..j] forms a palindrome. Note:Have to initialize a 2-D list in this way.If use 'A=[[False]*n]*n', every row will change as one row changes.
        cut=[n]*n                                                     #cut[i] means the minCut for s[i..n-1]
        i=n-1
        while i>=0:
            cut[i]=n-1-i
            for j in xrange(i,n):
                if s[i]==s[j] and (j-i<2 or A[i+1][j-1]):             #if s[i]==s[j] and s[i+1..j-1] is a palindrome or the length of s[i..j] less than 2, s[i..j] forms a palindrome, thus A[i][j] is True.
                    A[i][j]=True
                    if j==n-1:                                        #if j==n-1, the string s[i..n-1] is a palindrome, minCut is 0, cut[i]=0; 
                        cut[i]=0
                    elif cut[j+1]+1<cut[i]:                           #if the current cut num (first cut s[i..j] and then cut the rest s[j+1...n-1]) is 1+cut[j+1], compare it to the exisiting minCut num cut[i], repalce if smaller.
                        cut[i]=cut[j+1]+1
            i-=1
        return cut[0]                                                 #return minCut for s[0..n-1]
