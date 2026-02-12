class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0
        for i in range(len(s)):                          #Traverse s.
            count = Counter()                            #Initialize counter.
            for j in range(i, len(s)):                   #Traverse s[i:],
                count[s[j]] += 1                         #Update count[s[j]].
                if len(set(count.values())) == 1:        #If there is only one unique value in count.values(), s[i:j + 1] is a balanced substring; then update result if necessary.
                    result = max(result, j - i + 1)
        return result
