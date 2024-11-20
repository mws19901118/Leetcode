class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_count, window_count = Counter(s), Counter()                                                #Count characters in s, also count characters in sliding window.
        start, result = 0, len(s) + 1                                                                    #Initialize start of sliding window and the result to be a great number.
        for i, x in enumerate(s):                                                                        #Traverse s,
            window_count[x] += 1                                                                         #Increase window_count[x].
            while start <= i and any(window_count[y] > total_count[y] - k for y in ['a', 'b', 'c']):     #For any character y if window_count[y] > total_count[y] - k, it won't have enough occurence outside the sliding window. So move forward start while this condition is true and start is not greater than i.
                window_count[s[start]] -= 1                                                              #Decrease window_count[s[start]].
                start += 1
            if not any(window_count[y] > total_count[y] - k for y in ['a', 'b', 'c']):                   #If the condition is not true, update result if the sum of left part(start) and right part(len(s) - 1 - i) is smaller.
                result = min(result, start + len(s) - i - 1)
        return -1 if result == len(s) + 1 else result                                                    #Return -1 if result is still a great number; otherwise, return result.
