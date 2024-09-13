class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXOR = [0]                                                    #Initialize the prefix xor for arr.
        for x in arr:                                                      #Populate prefix xor for each index in arr.
            prefixXOR.append(prefixXOR[-1] ^ x)
        return [prefixXOR[x] ^ prefixXOR[y + 1] for x, y in queries]       #Since x ^ y ^ y = x, then just return prefixXOR[x] ^ prefixXOR[y + 1] for each query x and y.
