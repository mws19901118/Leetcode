from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)                                         #Count each character.
        segments = [(counts[k], k * counts[k]) for k in counts]     #Duplicate each character for the times of its count and put it together with its count in a tuple to form a list.
        segments.sort(reverse = True)                               #Sort the tuple list in desending order.
        result = ""                                                 #Add each segment in order to result.
        for s in segments:
            result += s[1]
        return result
