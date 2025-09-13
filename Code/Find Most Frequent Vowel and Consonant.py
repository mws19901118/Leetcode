class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)                                                                                #Count each letter.
        return max([count[x] for x in 'aeiou']) + max([count[x] for x in 'bcdfghjklmnpqrstvwxyz'])        #Add the max of vowel count and max of consonant count.
