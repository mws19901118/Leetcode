class Solution:
    def maximumLength(self, s: str) -> int:
        lengths = defaultdict(Counter)                        #Initialize a Counter for each character to count all possible length of special subarray.  
        i = 0
        while i < len(s):                                     #Traverse s.
            j = i + 1
            while j < len(s) and s[i] == s[j]:                #Find the length of current special subarray.
                j += 1
            length = j - i
            lengths[s[i]][length] += 1                        #Increase its count by 1.
            if length > 1:                                    #If length is greater than 1, increase the count of length - 1 by 2.
                lengths[s[i]][length - 1] += 2
            if length > 2:                                    #If length is greater than 2, increase the count of length - 2 by 3.
                lengths[s[i]][length - 2] += 3
            i = j                                             #Other lengths smaller than length - 2 won't be legit candidates. So, move i to j.
        result = -1
        for length in lengths.values():                       #Traverse each character.
            max_length = -1
            for k, v in length.items():                       #Find the max length whose count is greater than or equal to 3.
                if v >= 3:
                    max_length = max(max_length, v)
            result = max(result, max_length)                  #Update result if the max length of current character is longer.
        return result
        
