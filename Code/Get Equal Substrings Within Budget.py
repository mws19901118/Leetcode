class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start, end, result = 0, 0, 0                                  #Initialize start and end pointers for sliding window also result and cost
        while end < len(s):                                           #Iterate while end haven't reach the end.
            while end < len(s) and maxCost >= 0:                      #While end is valid and maxCost is not smaller than 0, change s[end] to t[end] and update the remaining budget then move forward end.
                maxCost -= abs(ord(s[end]) - ord(t[end]))
                end += 1
            result = max(result, end - start - int(maxCost < 0))      #Now the equal substrings in sliding windows are s[start:end - 1] and t[start:end - 1]; or s[start:end] and t[start:end] if maxCost >= 0.
            while start < end and maxCost < 0:                        #While start is smaller than end and maxCost is smaller than 0, restore s[start] and update the remaning budget then move forward start.
                maxCost += abs(ord(s[start]) - ord(t[start]))
                start += 1
        return result
            
