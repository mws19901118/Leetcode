class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1, c2 = collections.Counter(p), collections.Counter(s[:len(p)])        #Count each letter in p and each letter in s[:len(p)].
        result = []                                                             #Initialize result.
        if all(c1[x] == c2[x] for x in c1):                                     #If all letters in c1 has same count in c2, s[:len(p)] is an anagrams of p, so add 0 to result.
            result.append(0)
        for i in range(1, len(s) - len(p) + 1):                                 #Traverse from 1 to len(s) - len(p).
            c2[s[i + len(p) - 1]] += 1                                          #Move s[i - 1 + len(p)] out of c2.
            c2[s[i - 1]] -= 1                                                   #Move s[i - 1] in to c2.
            if all(c1[x] == c2[x] for x in c1):                                 #If all letters in c1 has same count in c2, s[i:i + len(p)] is an anagrams of p, so add i to result.
                result.append(i)
        return result                                                           #Return result.
