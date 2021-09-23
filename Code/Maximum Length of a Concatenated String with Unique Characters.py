class Solution:
    def dfs(self, binaryAndLength: List[tuple], concatenatedLength: int, mask: int) -> int:
        if not binaryAndLength:                                                                                 #If binaryAndLength is empty, return concatenatedLength.
            return concatenatedLength
        binary, length = binaryAndLength[0]                                                                     #Get the binary int and length of current string.
        result = self.dfs(binaryAndLength[1:], concatenatedLength, mask)                                        #Keep DFS without concatenating current string.
        if binary & mask == 0:                                                                                  #If binary & mask == 0, current string has no duplicate letter with concatenated string.
            result = max(result, self.dfs(binaryAndLength[1:], concatenatedLength + length, binary | mask))     #Keep DFS concatienating current string.
        return result                                                                                           #Return result
        
    def maxLength(self, arr: List[str]) -> int:
        noDup = [w for w in arr if all(v == 1 for k, v in Counter(w).items())]                                  #Remove all string containing duplicate letters.
        masks = {chr(ord('a') + x): (1 << x) for x in range(26)}                                                #Computer the binary mask for each letter.
        binaryAndLength = []                                                                                    #Use a list to store the binary int form of each string and string length.
        for w in noDup:                                                                                         #Traverse noDup.
            binary = 0
            for x in w:                                                                                         #Convert string to binary int.
                binary |= masks[x]
            binaryAndLength.append((binary, len(w)))                                                            #Append binary int and string length to binaryAndLength.
        return self.dfs(binaryAndLength, 0, 0)                                                                  #Start DFS.
