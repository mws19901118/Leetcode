class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordCounter, result = Counter(words), []                                                            #Count each word in words and initialize result.
        wordLength = len(words[0])                                                                          #Get the word length.
        for i in range(wordLength):                                                                         #Use a sliding window that moves forward word length characters each time, so we have to traverse all starting positions from 0 to wordLength - 1.
            left, right, visited = i, i, Counter()                                                          #Set the left and right(not inclusive in slinding window) pointers of sliding window and the counter of visited words.
            while right <= len(s):                                                                          #Iterate while right is not larger than length of s.
                currentWord = s[right:right + wordLength]                                                   #Get the new word just outside the sliding window.
                if currentWord not in wordCounter:                                                          #If current word is not in words, current slinding window won't have all words.
                    right += wordLength                                                                     #Move right to next word.
                    left, visited  = right, Counter()                                                       #Move left to right, also reset visited counter.
                    continue                                                                                #Continue iteration.
                while visited[currentWord] == wordCounter[currentWord]:                                     #While current word already visited max times in sliding window, move forward left until current word can be inserted in sliding wondow.
                    visited[s[left:left + wordLength]] -= 1                                                 #Update visited counter.
                    left += wordLength
                visited[currentWord] += 1                                                                   #Update visited counter.
                right += wordLength                                                                         #Move forward right.
                if right - left == len(words) * wordLength:                                                 #If the distance between left and right is exactly the concatenation of all words, then we found a legit starting index.
                    result.append(left)                                                                     #Append left to result.
                    visited[s[left:left + wordLength]] -= 1                                                 #Move forward left and update the visited counter.
                    left += wordLength
        return result                                                                                       #Return result.
