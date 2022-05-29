class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = {x: 1 << (ord(x) - ord('a')) for x in 'abcdefghijklmnopqrstuvwxyz'}                                                             #Initialize the bit masks for each letter.
        lengths = defaultdict(int)                                                                                                              #Store the max word length of each word bit mask.
        for w in words:                                                                                                                         #Traverse words.
            bitMask = 0
            for x in w:                                                                                                                         #Calculate the bit mask for each word.
                bitMask |= masks[x]
            lengths[bitMask] = max(len(w), lengths[bitMask])                                                                                    #Update the max word length of each bit mask.
        return max([lengths[x] * lengths[y] for x, y in product(lengths.keys(), lengths.keys()) if not x & y], default = 0)                     #Return the max product of word length of any 2 words not sharing common letter; if not found such pair, return 0.
