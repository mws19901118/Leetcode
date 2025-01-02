class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        count, vowels = 0, 'aeiou'                                            #Initialize count and vowels.
        prefixCount = [0]                                                     #Initialize prefix count.
        for w in words:                                                       #Populate prefix count.
            if w[0] in vowels and w[-1] in vowels:
                count += 1
            prefixCount.append(count)
        return [prefixCount[r + 1] - prefixCount[l] for l, r in queries]      #Return the result of each query.
