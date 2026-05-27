class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        indexes = defaultdict(list)                                                                        #Store the indexes of each number,
        for i, x in enumerate(word):
            indexes[x].append(i)
        count = 0                                                                                          #Initialize count.
        for i in range(26):                                                                                #Traverse from a to z.
            lower, upper = chr(ord('a') + i), chr(ord('A') + i)                                            #Calculate the lower case and upper case.
            if indexes[lower] and indexes[upper] and indexes[lower][-1] < indexes[upper][0]:               #If both has non empty indexes and the last of index of lower is smaller than the first index of upper, increase count.
                count += 1
        return count
