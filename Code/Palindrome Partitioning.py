class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start: int, stack: List[str]) -> None:
            if start == len(s):                                                             #If DFS reaches the end of string, append deep copy of current stack to result. 
                result.append(copy.deepcopy(stack))
                return
            for i in range(start, len(s)):                                                  #Traverse the string from the start index. 
                if s[i] == s[start] and (i <= start + 1 or dp[start + 1][i - 1]):           #If the current letter is the same of the letter in start index and s[start + 1:i] is palindrome or i <= start + 1, s[start:i + 1] is also a palindrome.
                    dp[start][i] = True                                                     #Update dp.
                    stack.append(s[start:i + 1])                                            #Add it to stack.
                    dfs(i + 1, stack)                                                       #DFS from i + 1.
                    stack.pop()                                                             #Pop stack.
        result = []
        dp = [[False for i in range(len(s))] for j in range(len(s))]                        #Initialize dp; dp[i][j] stores if s[i][j + 1] is palindrome. 
        dfs(0, [])                                                                          #DFS from the beginning.
        return result
