class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m = '#' + '#'.join(list(s)) + '#'                                               #Construct a new string so that each letter of s is between 2 '#'s in the new string.
        id = 0                                                                          #Record the index of midpoint of current longest palindrome.
        maxReach = 0                                                                    #Record the farest letter could be reached by current longest palindrome.
        p = [0] * len(m)                                                                #Record the max span length of palindrome at letter m[i] in new string.
        for i in range(len(m)):                                                         #Use Manacher's Algorithm to find the longest palindrome substring in m.
            if maxReach > i:
                p[i] = min(maxReach - i, p[id * 2 - i])
            else:
                p[i] = 1
            while i - p[i] >= 0 and i + p[i] < len(m) and m[i - p[i]] == m[i + p[i]]:
                p[i] += 1
            if i + p[i] > maxReach:
                maxReach = i + p[i]
                id = i
        for i in reversed(range(len(m))):                                               #Get the longest palindrome starting from the beginning.
            if p[i] == i + 1:
                return s[p[i] - 1:][::-1] + s                                           #Reverse the rest part and add it before then beginning.
