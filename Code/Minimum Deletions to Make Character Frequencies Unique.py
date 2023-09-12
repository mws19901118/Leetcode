class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(list(Counter(s).values()))               #Count character frequency in s and count the frequency.
        carry, result = 0, 0                                     #Initialize duplicated frequency carried over from last iteration and result.
        for x in reversed(range(1, max(count.keys()) + 1)):      #Iterate from the max frequency to 1.
            currentFrequency = count[x] + carry                  #Calculate current duplicate frequencies.
            carry = max(currentFrequency - 1, 0)                 #Then, currentFrequency - 1 frequencies flow to next iteration.
            result += max(0, currentFrequency - 1)               #We need to delete characters for currentFrequency - 1 characters to make current frequency unique.
        return result
