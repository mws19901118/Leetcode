class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        binaries = ["{0:08b}".format(x) for x in data]                                                                                            #Convert each number to 8-bit binary.
        i = 0
        while i < len(binaries):                                                                                                                  #Traverse binaries.
            index = binaries[i].find('0')                                                                                                         #Find the index of first 0.
            if index == 0:                                                                                                                        #If it's 0, the number is a one byte character, move to next.
                i += 1
            elif 2 <= index <= 4 and i + index - 1 < len(binaries) and all(binaries[j].startswith('10') for j in range(i + 1, i + index)):        #If it's between 2 and 4, the number is a n-bytes character.
                i += index                                                                                                                        #If next n - 1 numbers are not overflow and all starts with '10', they are valid and move to the number after them.
            else:                                                                                                                                 #Otherwise, it's not valid, return false.
                return False
        return True                                                                                                                               #Return true at the end.
