class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastConsonant(lowerLimit: int) -> int:                                        #Calculate the number of substrings which has at least lower limit consonants.
            result, start = 0, 0                                                             #Initialize result and start.
            count = Counter()                                                                #Count each vowel.
            vowels = set(['a', 'e', 'i', 'o', 'u'])                                          #Put vowels in a set.
            for i, x in enumerate(word):                                                     #Traverse word.
                count[x if x in vowels else 'c'] += 1                                        #If x is vowel, increase its corresponding count; otherwise, increase the count of 'c'.
                while all(count[v] >= 1 for v in vowels) and count['c'] >= lowerLimit:       #Iterate while all vowels have at least 1 count and consonant count is not smaller than the lower limit.
                    result += len(word) - i                                                  #Add len(word) - i to result because all the substrings starting at current start and ending at or beyond i will have all vowels at least once and at least lower limit consonants.
                    count[word[start] if word[start] in vowels else 'c'] -= 1                #If word[start] is vowel, increase its corresponding count; otherwise, increase the count of 'c'.
                    start += 1                                                               #Move forward start.
            return result
        return atLeastConsonant(k) - atLeastConsonant(k + 1)                                 #The final result is atLeastConsonant(k) - atLeastConsonant(k + 1).
