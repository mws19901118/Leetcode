class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary, result = set(words), []                                                                                                     #Store all words in set and initialize result.
        
        @cache                                                                                                                                  #Cache result
        def dfs(word: str, length: int) -> bool:                                                                                                #DFS.
            if length == len(word):                                                                                                             #If the length reaches the end of work, return true because it's completely spilt to several words in words list.
                return True
            return any(word[length:i] in dictionary and dfs(word, i) for i in range(length + 1, len(word) + 1 - (1 if not length else 0)))      #Traverse from length + 1 to len(word) + 1 - (1 if not length else 0), because we need at lease 2 words to concatenate, then check if any of word[length:i] is in dictionary and dfs(word, i) is true.

        return [w for w in words if dfs(w, 0)]                                                                                                  #Traverse each word and start dfs at the beginning of current word; if the result is true, add current word to result.
