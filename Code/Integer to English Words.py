class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        chunk = [1000000000, 1000000, 1000, 100]                        #Large number to split the num into 2 parts
        chunkword = ["Billion", "Million", "Thousand", "Hundred"]       #Word for large number
        basicword = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]    #Basic words for number less than 20
        roundtenword = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]     #Words for 20, 30, 40, 50, 60, 70, 80 and 90
        for i in range(4):
            if num >= chunk[i]:                             #Split large number into 2 parts, quotient and remainder.
                a = self.numberToWords(num/chunk[i])        #Get the word for quotient.
                b = self.numberToWords(num%chunk[i])        #Get the word for remainder.
                a += " " + chunkword[i]                     #Append the word for large number to a.
                if b != "Zero":                             #If b is not zero, append it to a.
                    a += " " + b
                return a
        if num < 100 and num >= 20:                         #Deal with number belonging to [20, 100)
            a = roundtenword[num/10 - 2]                    #Split it to tens digit and single digit, then get the word for tens digit.
            b = basicword[num%10]                           #Get the word for single digit.
            if b != "Zero":                                 #If b is not zero, append it to a.
                a += " " + b
            return a
        elif num < 20:                                      #If number is less than 20, directly return the word.
            return basicword[num]
