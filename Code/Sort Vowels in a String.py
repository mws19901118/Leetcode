class Solution:
    def sortVowels(self, s: str) -> str:
        letters = [x for x in s]                #Split s into letters.
        vowels = "AEIOUaeiou"                   #Initialize vowels in ASCII order.
        indexes, count = [], Counter()          #Store the index of vowels and count of each vowel.
        for i, x in enumerate(letters):         #Traverse letters to populate indexes and count.
            if x in vowels:
                indexes.append(i)
                count[x] += 1
        i = 0                                   #Initialize pointer.
        for x in vowels:                        #Traverse vowels.
            for _ in range(count[x]):           #For each vowel, put it on the index of pointer for x times, x is the count of vowel.
                letters[indexes[i]] = x
                i += 1                          #Move pointer forward.
        return "".join(letters)                 #Join letters and return.
