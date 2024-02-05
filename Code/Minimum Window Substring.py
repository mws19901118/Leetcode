class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, countS = Counter(t), Counter()                                  #countT counts the characters in t, and countS counts the characters in sliding window, initially empty.
        start, end = 0, 0                                                       #The start and end of sliding window.
        result = ""                                                             #Store result.
        found = 0                                                               #Store how many distinct characters have been satisfied in sliding window.
        while end < len(s):                                                     #While the sliding window haven't reached the end of s, find the rightmost end for current start.
            while end < len(s) and found < len(countT):                         #While not all charcters of t has been satisfied in sliding window.
                countS[s[end]] += 1                                             #Update count of s[end] in sliding window.
                found += (countS[s[end]] == countT[s[end]])                     #If s[end] is in t and the count of s[end] is same in both sliding window and t, one more character of t is satisfied.
                end += 1                                                        #Move end to next character.
            
            if found < len(countT):                                             #If sliding window reaches end of s but not all characters in t has been satisfied, break.
                break
            
            while start < end and found == len(countT):                         #While all charcters of t has been satisfied in sliding window, find the rightmost start for current end.
                found -= (countS[s[start]] == countT[s[start]])                 #If s[end] is in t and the count of s[end] in sliding window is smaller than that in t, one less character of t is satisfied.
                countS[s[start]] -= 1                                           #Update count of s[end] in sliding window.
                start += 1                                                      #Move start to next character.
                
            if not result or len(result) > len(s[start - 1:end]):               #Update result if needed.
                result = s[start - 1:end]
        return result
