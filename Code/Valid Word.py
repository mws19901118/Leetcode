class Solution:
    def isValid(self, word: str) -> bool:
        return len(word) >= 3 and word.isalnum() and bool(set(word) & set("aeiouAEIOU")) and bool(set(word) & set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"))  #Check each condition.
