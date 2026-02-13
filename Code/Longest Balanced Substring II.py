class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0
        i = 0                                                                  #First, check the longest balanced substring with only 1 letter, i.e. longest substring with same consecutive letter.
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            result = max(result, j - i)
            i = j
        pairs = [('a', 'b'), ('b', 'c'), ('c', 'a')]                           #Second, for each pair, check the longest balanced substring with only the 2 letters in current pair.
        for x, y in pairs:
            i = 0
            while i < len(s):
                j = i
                count, index = 0, {0: i - 1}                                   #Store the first index of relative count.
                while j < len(s) and s[j] in (x, y):
                    count += (1 if s[j] == x else -1)
                    if count in index:
                        result = max(result, j - index[count])
                    else:
                        index[count] = j
                    j += 1
                i = j
                if i < len(s) and s[i] not in (x, y):
                    i += 1
        i = 0                                                                  #Finally, check the longest balanced substring with all 3 letter.
        countAminusC, countBminusC, index = 0, 0, {(0, 0): -1}                 #Use relative counts as well, but this time it is 2 letters against 1 letter.
        for i, x in enumerate(s):
            if x == 'a':                                                       #Update relative counts.
                countAminusC += 1
            elif x == 'b':
                countBminusC += 1
            else:
                countAminusC -= 1
                countBminusC -= 1
            if (countAminusC, countBminusC) in index:
                result = max(result, i - index[(countAminusC, countBminusC)])
            else:
                index[(countAminusC, countBminusC)] = i
        return result
