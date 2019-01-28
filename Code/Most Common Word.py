import re
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)                                #Create a set for banned words and add empty string to it.
        banned.add("")
        words = re.split(r"[!?',;. ]+", paragraph.lower())  #Convert the paragraph to lower case and split it by punctuation and space.
        counter = Counter(words)                            #Count the words.
        mostCommon = ""
        maxCount = 0
        for w in counter:
            if counter[w] > maxCount and w not in banned:   #If a word is not banned, check if it's count is the highest.
                mostCommon = w
                maxCount = counter[w]
        return mostCommon
