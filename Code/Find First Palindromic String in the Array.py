class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:                                                      #Traverse words.
            if all(w[i] == w[-(i + 1)] for i in range(len(w) // 2)):         #Determine if current word is palindrome.
                return w                                                     #If it is then return it.
        return ""                                                            #Return "" if not found.
