class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])                 #Store vowels in a set.
        result, count = 0, 0                                    #Initialize result and count.
        for i, x in enumerate(s):                               #Traverse s.
            if x in vowels:                                     #if x in vowels, increase count.
                count += 1
            if i - k >= 0 and s[i - k] in vowels:               #If i - k >= 0 and s[i - k] vowels, decrease count.
                count -= 1
            result = max(result, count)                         #Update result if necessary.
        return result                                           #Return result.
