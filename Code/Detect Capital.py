class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or not word[1:] or word[1:].islower()     #Word should be all uppercase or only one character or all lowercase after first character.
