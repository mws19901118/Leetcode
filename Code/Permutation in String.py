class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter, s2Counter = Counter(s1), Counter(s2[:len(s1)])           #Count each letter in s1 and s2[:len(s1)].
        for i in range(len(s1), len(s2) + 1):                               #Traverse from the len(si)-th letter in s2 to the end of s2.
            if all(s1Counter[x] == s2Counter[x] for x in s1Counter):        #If all letters in s1Counter has same count in s2Counter, s2[i - len(s1):i] is a permutation of s1, so return true.
                return True
            s2Counter[s2[i]] += 1                                           #Update s2Counter to count each letter in s2[i - len(s1):i].
            s2Counter[s2[i - len(s1)]] -= 1
        return all(s1Counter[x] == s2Counter[x] for x in s1Counter)         #Check if the s2[len(s2) - len(s1):] is a permutation of s1.
