class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [x for x in queries if any(sum(u != v for u, v in zip(x, y)) <= 2 for y in dictionary)]      #Traverse queries and add word to result if it has edit distance smaller than or equal to with any word in dictionary.
