class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        count = Counter()                                                                                           #Count each character in s2.
        curr = ('', 0)                                                                                              #Store current character and its count.
        prev = {}                                                                                                   #Store the previous character and its count of current character and its count.
        for i, x in enumerate(s2):                                                                                  #Traverse s2.
            count[x] += 1                                                                                           #Increase count of x.
            prev[(x, count[x])], curr = curr, (x, count[x])                                                         #Update curr and set prev[curr].
        
        result = ""                                                                                                 #Initialize result.
        dp = defaultdict(list)                                                                                      #Initialize dp, dp[x][c] means the earlist window starting index that contains subsequence from the begining of s2 to the (c + 1)th occurrence of x.
        for i, x in enumerate(s1):                                                                                  #Traverse s1.
            for c in reversed(range(1, count[x] + 1)):                                                              #Traverse count[x] to 1 reversely.
                prevCharacter, prevCount = prev[(x, c)]                                                             #Get the prev character and its count of current character and its count.
                if len(dp[prevCharacter]) < prevCount:                                                              #If len(dp[prevCharacter]) < prevCount, not window contains the subsequence from the begining of s2 to prev character of the (c + 1)th occurrence of x, so continue.
                    continue
                startingIndex = dp[prevCharacter][prevCount - 1] if prevCount else i                                #Get the starting index, dp[prevCharacter][prevCount - 1] if prev character is valid, otherwise, i is the starting index.
                if len(dp[x]) < c:                                                                                  #Update dp[x][c - 1] to starting index.
                    dp[x].append(startingIndex)
                else:
                    dp[x][c - 1] = startingIndex
                if x == s2[-1] and c == count[x]:                                                                   #If (c + 1)th occurrence of x count be the end of s2, update result to be s1[dp[x][c - 1]:i + 1] if it is empty or its length is greater than i - dp[x][c - 1] + 1.
                    if not result or len(result) > i - dp[x][c - 1] + 1:
                        result = s1[dp[x][c - 1]:i + 1]
        return result                                                                                               #Return result.
