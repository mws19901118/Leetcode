class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter()                                      #Count each character.
        for w in words:
            for x in w:
                c[x] += 1
        return all(not c[x] % len(words) for x in c)       #Return if the count of every character can be divided by the length of words, so every character can be distributed evenly.
