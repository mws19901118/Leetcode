class Solution:
    def backtrack(self, n: int, p: List[str], count: int, result: List[str]):
        if len(p) == 2 * n:                                                     #If current length is 2 * n, the backtracking comes to an end.
            if count == 0:                                                      #If there is no unmatched left parentheses, we find a combination of valid parentheses.
                result.append("".join(p))                                       #Append current answer to result.
            return
        if count < n:                                                           #Only when count < n can we add left parenthesis at current position.
            p.append('(')
            self.backtrack(n, p, count + 1, result)                             #Add a left parenthesis and keep backtracking.
            p.pop()
        if count > 0:                                                           #Only when count > 0 can we add right parenthesis at current position.
            p.append(')')
            self.backtrack(n, p, count - 1, result)                             #Add a right parenthesis and keep backtracking.
            p.pop()
            
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(n, [], 0, result)                                        #Backtracking.
        return result

class Solution:
    @cache                                                                      #Cache result.
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:                                                              #If n == 1, return one pair of parenthesis.
            return ["()"]
        parenthesis = set()                                                     #Use a set to store valid parenthesis of length n.
        for i in range(1, (n + 1) // 2 + 1):                                    #Traverse from 1 to n / 2.
            for p1 in self.generateParenthesis(i):                              #Get all valid parenthesis for i.
                for p2 in self.generateParenthesis(n - i):                      #Get all valid parenthesis for n - i.
                    parenthesis.add(p1 + p2)                                    #Add p1 + p2 to set.
                    parenthesis.add(p2 + p1)                                    #Add p2 + p1 to set.
        for p in self.generateParenthesis(n - 1):                               #Get all valid parenthesis for n - 1.
            parenthesis.add("(" + p + ")")                                      #Add (p) to set.
        return parenthesis                                                      #Return set.
