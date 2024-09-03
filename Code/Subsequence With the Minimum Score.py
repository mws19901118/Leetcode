class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m, n = len(s), len(t)                                                #Get the length of s and t.
        leftMost, rightMost = [-1] * n, [-1] * n                             #Initialize leftMost and rightMost to be length n and all -1.
        j = 0
        for i in range(n):                                                   #Traverse s and t from front to behind to populate leftMost; leftMost[i] is the leftmost index k in s so that t[:i + 1] is a subsequence of s[:k + 1].
            while j < m and s[j] != t[i]:                                    #While j is valid and s[j] != t[i], move forward j.
                j += 1
            if j < m:                                                        #If j is still valid, update leftMost[i] and move forward j.
                leftMost[i] = j
                j += 1
        
        j = m - 1
        for i in reversed(range(n)):                                         #Traverse s and t from behind to front to populate rightMost; rightMost[i] is the rightmost index k in s so that t[j:] is a subsequence of s[k:].
            while j >= 0 and s[j] != t[i]:                                   #While j is valid and s[j] != t[i], move backward j.
                j -= 1
            if j >= 0:                                                       #If j is still valid, update rightMost[i] and move backward j.
                rightMost[i] = j
                j -= 1

        left = -1                                                            #Initialize left.
        for i in range(n):                                                   #Find the largest left so that leftMost[left] is not -1.
            if leftMost[i] == -1:
                break
            left = i
        result = n - left - 1                                                #Now t[:left + 1] is a subsequence of s. Suppose all the characters after left have to be removed, then result is n - 1 - (left + 1) + 1 = n - left - 1.
        for right in reversed(range(n)):                                     #Enumerate possible right index from behind to front so that t[right:] don't have to be removed.
            if rightMost[right] == -1:                                       #If rightMost[right] == -1, there won't be anymore right that could fulfil the condition, so jump out of the loop.
                break
            left = min(left, right - 1)                                      #Left must be smaller than right
            while left >= 0 and leftMost[left] >= rightMost[right]:          #Move back left to guarantee leftMost[left] < rightMost[right]; otherwise there would be intersenction between s[:leftMost[left] + 1] and s[rightMost[right]] then we cannot guarantee t[:left + 1] + t[right:] is still a subsequence of s.
                left -= 1
            result = min(result, right - left - 1)                           #Update result if (right - 1) - (left + 1) + 1 = right - left - 1 is smaller.
        return result
