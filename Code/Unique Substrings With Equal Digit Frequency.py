class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        count = 0                                                              #Count valid substrings.
        for l in range(1, len(s) + 1):                                         #Enumerate the length of substring.
            h = int(s[:l])                                                     #Initialize the hash as int(s[:l]).
            counter = Counter(s[:l])                                           #Count each digit.
            highest_bit = 10 ** (l - 1)                                        #Calculate the highest bit mask.
            visited = set()                                                    #Store visited valid substrings.
            if len(set(counter.values())) == 1:                                #If current substring has same frequency for each digit, add it to visited.
                visited.add(h)
            for i in range(l, len(s)):                                         #Moving forward the sliding window.
                h = (h - int(s[i - l]) * highest_bit) * 10 + int(s[i])         #Update rolling hash.
                counter[s[i - l]] -= 1                                         #Update frequency in the substring.
                counter[s[i]] += 1
                if len(set(counter.values()) - set([0])) == 1:                 #If it is valid, add it to visited.
                    visited.add(h)
            count += len(visited)                                              #The size of visited is the valid substrings of current length.
        return count
