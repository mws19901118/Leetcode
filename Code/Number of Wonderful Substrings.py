class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitMasks = {x: 1 << (ord(x) - ord('a')) for x in "abcdefghij"}                                            #Create a bit mask for each letter.
        prefixMask, result = 0, 0                                                                                 #Initialize a prefixMask, which is 0 initially, and the result.
        maskCount = defaultdict(int)                                                                              #Count each prefixMask.
        maskCount[0] = 1
        for x in word:                                                                                            #Traverse word.
            prefixMask ^= bitMasks[x]                                                                             #Prefix mask xor with the bit mask of current letter, So, if a bit is 1, it means the substring from start to current letter has an odd count of the corresponding letter.
            result += maskCount[prefixMask] + sum(maskCount[prefixMask ^ y] for y in bitMasks.values())           #Add maskCount[prefixMask] to result, because for each substring from the end of previous prefix mask to current letter contains only even count letters. Also add the count of each mask which is 1 bit different with current prefix mask, meaning the substring has only 1 odd count letter.
            maskCount[prefixMask] += 1                                                                            #Increase maskCount[prefixMask].
        return result
