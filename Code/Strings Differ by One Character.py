class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):                  #Enumreate each index of word.
            s = set()                                  #Store seen pattern using set.
            for w in dict:                             #Traverse dict.
                pattern = w[:i] + "*" + w[i + 1:]      #Replace character on current index with "*" to generate a pattern.
                if pattern in s:                       #If pattern is seen, return true.
                    return True
                s.add(pattern)                         #Add pattern to s.
        return False                                   #Return False at the end.
