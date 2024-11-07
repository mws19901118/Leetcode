class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = Counter()              #Count the occurrence of each digit from least significant to most significant.
        for x in candidates:           #Traverse candidates.
            i = 0                      #Initialize the bit index.
            while x:                   #Traverse bits of x from least significant to most significant.
                count[i] += x & 1      #Increase count[i] if current bit is 1.
                x >>= 1                #Right shift x.
                i += 1                 #Increase i.
        return max(count.values())     #Return the largest values in count, which means the size of combination.
