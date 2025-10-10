class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result = -inf                                #Initialize result.
        for i in range(k):                           #Traverse from 0 to k - 1.
            index, x = len(energy) - 1 - i, 0        #Enumerate each ending index at len(energy) - 1 - i; also initialize the energy.
            while index >= 0:                        #Move backward to enumerate the starting index given the ending index.
                x += energy[index]                   #Get energy[index].
                index -= k                           #Move backward k steps.
                result = max(result, x)              #Update result if necessary.
        return result
