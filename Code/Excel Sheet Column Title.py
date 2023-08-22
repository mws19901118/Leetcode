class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''                                                #Initialize title.
        while columnNumber:                                       #Iterate while columnNumber is greater than 0.
            columnNumber -= 1                                     #Decrease column number to handle carry; because for example from 'Z' to 'AA', it increase 1 but looks like 2(analogy to '9' and '11').
            title += chr((columnNumber) % 26 + ord('A'))          #Convert like converting base 10 number to base 26 number.
            columnNumber //= 26
        return title[::-1]                                        #Return the reverse of title.
