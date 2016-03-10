class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dict = {}                                                                     #Store the original index of each word.
        t = []                                                                        #Store the answers in a list of tuple.                                 
        for i in range(len(words)):
            dict[words[i]] = i
        for i in range(len(words)):                                                   #For each word, check every index form 0 to len(words[i]).
            for j in range(len(words[i]) + 1):
                first = words[i][:j]                                                  #Get the first half.
                second = words[i][j:]                                                 #Get the second half.
                rfirst = first[::-1]                                                  #Reverse the first half.
                rsecond = second[::-1]                                                #Reverse the second half.
                if first == rfirst and rsecond != words[i] and rsecond in dict:       #If the first is palindrome and rsecond is not words[i] it self and rsecond is in dict, append the index of rsecond and current index as a tuple to t.
                    t.append((dict[rsecond], i))
                if second == rsecond and rfirst != words[i] and rfirst in dict:       #If the second is palindrome and rfirst is not words[i] it self and rfirst is in dict, append current index and the index of rfirst as a tuple to t.
                    t.append((i, dict[rfirst]))
        t = list(set(t))                                                              #Remove all the duplicates.
        result = []
        for x in t:
            result.append([x[0], x[1]])                                               #Convert from tuple to list of integers.
        return result                                                                 #Return result.
