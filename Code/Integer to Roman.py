class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):          #Use a table to store Roman numeral corresponding to each digit.
        table=[['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]
        roman=""
        for i in range(3,-1,-1):
            roman+=table[i][num/10**i]  #Convert the integer to Roman numeral digit by digit.
            num%=10**i
        return roman
