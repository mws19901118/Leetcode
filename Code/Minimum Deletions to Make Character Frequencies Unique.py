class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(list(Counter(s).values()))          #Count character frequency in s and count the frequency.
        maxFrequency = max(count.keys())                    #Find the max frequency.
        carry = 0                                           #Initialize duplicated frequency carried over from last iteration.
        result = 0                                          #Initialize result.
        for x in reversed(range(1, maxFrequency + 1)):      #Iterate from maxFrequency to 1.
            currentFrequency = count[x] + carry             #Calculate current duplicate frequencies.
            result += max(0, currentFrequency - 1)          #We need to delete characters for currentFrequency - 1 characters to make current frequency unique.
            carry = max(currentFrequency - 1, 0)            #Then, currentFrequency - 1 frequencies flow to next iteration.
        return result
