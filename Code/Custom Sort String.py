class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count = Counter(str)                        #Count each letter in str.
        sortedStr = ""                              #Initialize sorted str.
        for x in order:                             #Traverse order.
            if x in count:                          #If x is in str, add all its occurence to sortedStr and delete it from count.
                sortedStr += x * count[x]
                del count[x]
        for x in count:                             #Traverse remaining count.
            sortedStr += x * count[x]               #Add all its occurence to sortedStr.
        return sortedStr                            #Return sorted str.
