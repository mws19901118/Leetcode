class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last0Index = [-1] * (len(s) + 1)                                                  #Initialize and populate the index of last 0 at each index after adding a virtual 0 at the beginning.
        for i in range(len(s)):
            if i == 0 or s[i - 1] == "0":
                last0Index[i + 1] = i
            else:
                last0Index[i + 1] = last0Index[i]

        result = 0
        for i in range(1, len(s) + 1):                                                    #Traverse each index.
            count0 = 1 if s[i - 1] == "0" else 0                                          #Initialize count 0 in current window.
            j = i                                                                         #Initialize j as the start of window.
            while j > 0 and count0 * count0 <= len(s) - count0:                           #Iterate while the square of count 0 is not breaching the upper bound(len(s) - count 0).
                count1 = (i - last0Index[j]) - count0                                     #Calculate the max count 1 in the window that ends at i and contains exactly count 0 of 0.
                if count0 * count0 <= count1:                                             #If the square of count 0 is not larger than count 1,
                    result += min(j - last0Index[j], count1 - count0 * count0 + 1)        #Add the possible number start of dominant ones substrings which end at i. The possible number is the smaller of j - last0Index[j](constraint of possible start) and count1 - count0 * count0 + 1(constriant of dominant ones).
                j = last0Index[j]                                                         #Move j to that last 0 index at j.
                count0 += 1                                                               #Increase count 0.
        return result
