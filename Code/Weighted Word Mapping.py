class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(chr(ord('a') + 25 - sum(weights[ord(x) - ord('a')] for x in w) % 26) for w in words)      #Calculate the weight of each word then convert to letter using reverse alphabetical order. Then join together and return.
