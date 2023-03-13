class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:                                                             #If length of s is shorted than 10, return an empty list.
            return []
        value = {'A': 0, 'C': 1, 'G': 2, 'T': 3}                                    #Encode each type of nucleotide in a base 4 number. 
        hash = 0                                                                    #Generate hash for the first 10 nucleotides.
        for i in range(10):
            hash = hash * 4 + value[s[i]]
        count = Counter()                                                           #Store the hash of each sequence in counter.
        count[hash] += 1
        mask = 4 ** 9                                                               #Initialize a mask for length of 9.
        result = []
        for i in range(10, len(s)):                                                 #Traverse from index 10 to the end.
            hash = hash % mask * 4 + value[s[i]]                                    #Compute rolling hash.
            if count[hash] == 1:                                                    #If hash occurs once, append the current sequence to result.
                result.append(s[i - 9:i + 1])
            count[hash] += 1                                                        #Increase count of hash.
        return result
