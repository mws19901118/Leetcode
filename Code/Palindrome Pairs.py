class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {x: i for i, x in enumerate(words)}                                #Store the original index of each word.
        t = set()                                                              #Store the answers in a set of tuple.                                 
        for i, w in enumerate(words):                                          #For each word, check every index form 0 to len(words[i]).
            for j in range(len(w) + 1):
                first, second = w[:j], w[j:]                                   #Get the first and second half.
                rfirst, rsecond = first[::-1], second[::-1]                    #Reverse the first and second half.
                if first == rfirst and rsecond != w and rsecond in d:          #If the first is palindrome and rsecond is not words[i] it self and rsecond is in d, append the index of rsecond and current index as a tuple to t.
                    t.add((d[rsecond], i))
                if second == rsecond and rfirst != w and rfirst in d:          #If the second is palindrome and rfirst is not words[i] it self and rfirst is in d, append current index and the index of rfirst as a tuple to t.
                    t.add((i, d[rfirst]))
        return list(t)
