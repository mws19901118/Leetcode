class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0                                                                         #The start of 2 pointers on name.
        j = 0                                                                         #The start of 2 pointers on typed.
        while i < len(name):
            count = 1
            while i + count < len(name) and name[i + count] == name[i + count - 1]:   #Count the consective length of each charcters in name.
                count += 1
            typedCount = 0
            while j + typedCount < len(typed) and typed[j + typedCount] == name[i]:   #Count the consective length of the corresponding character in typed.
                typedCount += 1
            if typedCount < count:                                                    #If the consective length in typed is smaller than the sonsective length, then return false.
                return False
            else:                                                                     #Otherwise update the start of 2 pointers in name and typed.
                i += count
                j += typedCount
        return j == len(typed)                                                        #After one pass in name, determine if there are remaining characters in typed.
