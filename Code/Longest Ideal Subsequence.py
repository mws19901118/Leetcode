class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lengthByLastLetter = [0] * 26                                          #For each letter, store the longest ideal subsequence ending at it 
        for x in s:                                                            #Traverse s.
            length = 1                                                         #Initialize length of ideal subsequence ending at current letter.
            curr = ord(x) - ord('a')                                           #Get the corresponding integer for current letter.
            for i in range(max(0, curr - k), min(26, curr + k + 1)):           #Traverse the letters whose absolute distance with curr is at most k and is valid.
                length = max(length, lengthByLastLetter[i] + 1)                #We could extend the ideal subsequence ending at i to curr, so update length if necessary.
            lengthByLastLetter[curr] = length                                  #Update lengthByLastLetter[curr] to length.
        return max(lengthByLastLetter)                                         #Return the max of lengthByLastLetter.
