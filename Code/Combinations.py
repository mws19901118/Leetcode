class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def backtrack(i,j):                     #Backtracking search; i is the current length and j is the current position.
            if i==k:
                temp=[]
                for c in stack:                 #Deep copy.
                    temp.append(c)
                result.append(temp)             #Append temp to result.
            else:
                for v in range(j+1,n-k+i+2):    #Traverse all the possible value.
                    stack.append(v)             #Push stack.
                    backtrack(i+1, v)           #Backtracking search next value.
                    stack.pop()                 #Pop stack.
        result=[]
        if n==0:
            return []
        stack=[]
        backtrack(0, 0)                         #Start from length 0 and position 0.
        return result
