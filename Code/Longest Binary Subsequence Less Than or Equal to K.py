class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        b, count = 0, 0                      #Initialize the binary integer of longest subsequence and count.
        for i, x in enumerate(s[::-1]):      #Traverse s backwards.
            if x == "1":                     #If x is 1, check if adding 1 in the front of subsequence will lead to the subsequence greater than k.
                if b + (1 << i) <= k:        #If not, then add 1 in the front and increase count. Thus we always add 1 at lower bits.
                    b += 1 << i
                    count += 1
            else:                            #If x is 0, just add 0 in the front as there could be leading zeros.
                count += 1
        return count
