class Solution:
    def isSubsequence(self, longStr: str, shortStr: str) -> bool:                           #Check if shortStr is a subsequence of longStr.
        j = 0
        for i, x in enumerate(longStr):
            if j < len(shortStr) and x == shortStr[j]:
                j += 1
        return j == len(shortStr)
    
    def findLUSlength(self, strs: List[str]) -> int:
        strsByLength = defaultdict(list)                                                    #Group strings by its length.
        for s in strs:
            strsByLength[len(s)].append(s)
        sortedLength = sorted(strsByLength.keys(), reverse = True)                          #Sort the lengths in descending order.
        longerStr = []                                                                      #Initalize the strings longer(actually not shorter) than current string.
        for x in sortedLength:                                                              #Traverse string lengths.
            count = Counter(strsByLength[x])                                                #Count strings.
            for s in count:                                                                 #Traverse de-duped strings.
                if any(self.isSubsequence(longStr, s) for longStr in longerStr):            #If s is subsequence of any string in longerStr, continue.
                    continue  
                if count[s] > 1:                                                            #If count[s] > 1, append it to longerStr.
                    longerStr.append(s)
                else:                                                                       #Otherwise return x because it's not subsequence of any other string. The longest uncommon subsequence must be a string it self. Because if a string is a subsequence of another string, all its subsequence will also be subsequences of another string.
                    return x
        return -1                                                                           #Return -1 after traverse.
