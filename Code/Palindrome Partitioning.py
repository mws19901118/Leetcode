class Solution:
    def dfs(self, s: str, start: int, stack: List[str], dp: List[List[bool]], result: List[List[str]]) -> None:
        if start == len(s):                                                             #If DFS reaches the end of string, append deep copy of current stack to result. 
            result.append(copy.deepcopy(stack))
            return
        for i in range(start, len(s)):                                                  #Traverse the string from the start index. 
            if s[i] == s[start] and (i <= start + 1 or dp[start + 1][i - 1]):           #If the current letter is the same of the letter in start index and s[start + 1:i] is palindrome or i <= start + 1, s[start:i + 1] is also a palindrome.
                dp[start][i] = True                                                     #Update dp.
                stack.append(s[start:i + 1])                                            #Add it to stack.
                self.dfs(s, i + 1, stack, dp, result)                                   #DFS from i + 1.
                stack.pop()                                                             #Pop stack.
    def partition(self, s: str) -> List[List[str]]:
        result = []
        dp = [[False for i in range(len(s))] for j in range(len(s))]                    #Initialize dp; dp[i][j] stores if s[i][j + 1] is palindrome. 
        self.dfs(s, 0, [], dp, result)                                                  #DFS from the beginning.
        return result
