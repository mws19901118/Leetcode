class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def largestSuffix() -> str:                                     #Find the lexicographically largest suffix of word.
            i, j, n = 0, 1, len(word)                                   #Initialize 2 points i(start of current suffix) at 0 and j(start of next possible larger suffix) at 1.
            while j < n:                                                #Iterate while j is smaller than the length of word, n.
                k = 0
                while j + k < n and word[i + k] == word[j + k]:         #Find the smallest k such that word[j + k] is valid and does not equal to word[i + k].
                    k += 1
                if j + k < n and word[i + k] < word[j + k]:             #If such k exists and word[i + k] < word[j + k], suffix word[j:] will be larger than suffix word[i:].
                    i, j = j, max(j + 1, i + k + 1)                     #So, move i to j and move j to the max of j + 1 and i + k + 1. Because for any index x between i and i + k + 1(exclusive), word[x] won't be greater than word[i] and word[x:i + k + 1] won't be greater than the substring with same length and starting at j. But, i + k + 1 might be smaller than j + 1, so we take the greater.
                else:                                                   #Otherwise, move j to j + k + 1.
                    j = j + k + 1                                       #Because for any index x before that, word[x] won't be greater than word[i] and word[x:j + k + 1] won't be greater than the substring with same length and starting at i.
            return word[i:]                                             #Return word[i:].

        if numFriends == 1:                                             #If numFriends is 1, word cannot be split, so return word itself.
            return word
        suffix = largestSuffix()                                        #Find the largest suffix of word
        return suffix[:min(len(last), len(word) - numFriends + 1)]      #Return the max length prefix of the suffix. 
                                                                        #Max kength is len(word) - numFriends + 1 so that there are enough substrings for other friends.
                                                                        #If max length is greater than the suffix, return the suffix itself.
