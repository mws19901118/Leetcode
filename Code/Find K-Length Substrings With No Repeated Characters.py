class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):                            #If k is greater than length of s, return 0 directly.
            return 0
        count = Counter(s[:k])                    #Count the first k characters in s.
        result = int(len(count) == k)             #Initialize result to be if count has exactly k characters.
        for i in range(k, len(s)):                #Traverse from k to end of s.
            count[s[i]] += 1                      #Increase count of s[i].
            count[s[i - k]] -= 1                  #Decrease count of s[i - k].
            if not count[s[i - k]]:               #If count[s[i - k]] is 0, pop s[i - k] from count.
                count.pop(s[i - k])
            result += int(len(count) == k)        #Increase result f count has exactly k characters.
        return result
