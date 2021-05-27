class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lengths = defaultdict(int)
        for s in words:
            binary = 0
            for c in s:
                binary |= 1 << (ord(c) - ord('a'))                  #Map the letter set of a string to a 26-bit binary. Each bit indicates if the string has correspoding letter.
            lengths[binary] = max(lengths[binary], len(s))          #For every binary, only store the length of the longest string.
        result = 0
        for x, lx in lengths.items():                               #Traverse through every binary pair.
            for y, ly in lengths.items():
                if x & y == 0:                                      #If x & y == 0, the 2 strings don't share common letter.
                    result = max(result, lx * ly)                   #Update the max product.
        return result
