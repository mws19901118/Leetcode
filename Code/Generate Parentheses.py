class Solution:
    def backtrack(self, n, p, count, result):
        if len(p)==2*n:                           #If current length is 2*n, the backtracking comes to an end.
            if count==0:                          #If there is no unmatched left parentheses, we find a combination of well-formes parentheses.
                result.append("".join(p))         #Append current answer to result.
        else:
            if count<n:                           #Only when count<n can we add left parenthesis at current position.
                p.append('(')
                count+=1                          #Adding a left parenthesis means here comes a new unmatched left parenthesis.
                self.backtrack(n,p,count,result)
                p.pop()
                count-=1
            if count>0:                           #Only when count>0 can we add right parenthesis at current position.
                p.append(')')
                count-=1                          #Adding a right parenthesis means there is an unmatched left parenthesis being matched.
                self.backtrack(n,p,count,result)
                p.pop()
                count+=1
            
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        p=[]                                      #Record current sequence of parentheses.
        count=0                                   #Record the number of unmatched left parentheses.
        result=[]
        self.backtrack(n,p,count,result)          #Backtrack.
        return result
