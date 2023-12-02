class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)                                      #Count each character in chars.
        def canForm(word: str) -> bool:                             #Determine if a word can be formed by characters.
            c = Counter(word)                                       #Count each character in word.
            return all(c[x] <= count[x] for x in c)                 #Every character count should not exceed that in count of chars.
        return sum(len(w) for w in words if canForm(w))             #Sum up the length of all such word in words.
