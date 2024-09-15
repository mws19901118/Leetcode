class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masks = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}      #Assign a bit mask for each vowel.
        prefix, result = 0, 0                                  #Initialize the xor prefix and result.
        indexes = {0:-1}                                       #Initially, there is no vowel, so the prefix is 0 and give it an index -1.
        for i, x in enumerate(s):                              #Traverse s.
            if x in 'aeiou':                                   #If x is vowel, xor prefix with its mask to update prefix, so if an vowel is seen odd times, its bit will be 1; otherwise, the bit will be 0.
                prefix ^= masks[x]
            if prefix in indexes:                              #If prefix is seen, fron its first index(not included) to i, each vowel has even count.
                result = max(result, i - indexes[prefix])
            else:                                              #Set indexes[prefix] to i to store the first index of any prefix.
                indexes[prefix] = i
        return result
