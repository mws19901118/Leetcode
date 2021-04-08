class Solution:
    def dfs(self, digitToLetter: dict, digits: str, result: List[str], stack: List[str]) -> None:
        if not digits:                                                                                                          #If reaches the end of digits, join stack and append to result if stack is not empty, then return.
            if stack:
                result.append("".join(stack))
            return
        for x in digitToLetter[digits[0]]:                                                                                      #Traverse the corresponding letters of current digit.
            stack.append(x)                                                                                                     #Append the letter to the stack.
            self.dfs(digitToLetter, digits[1:], result, stack)                                                                  #Keep DFS next digit.
            stack.pop()                                                                                                         #Pop stack.
            
    def letterCombinations(self, digits: str) -> List[str]:
        digitToLetter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}      #Map digits to characters.
        result=[]
        self.dfs(digitToLetter, digits, result, [])                                                                             #Begin backtracking with index=h0.
        return result                                                                                                           #Return result.
