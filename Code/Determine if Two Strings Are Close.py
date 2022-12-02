class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)                                                     #Count the letters in each string.
        return count1.keys() == count2.keys() and Counter(count1.values()) == Counter(count2.values())          #Because Operation 1 allows us to freely reorder the string, so close strings must consist of same set of letters. Because Operation 2 allows us to freely reassign the letters' frequencies, so the count of count must be same.
